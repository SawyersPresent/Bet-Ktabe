# Mutator Kit

Over the past few years there has been a massive proliferation of YARA signatures for Beacon. These typically tend to target the static components of Beacon, such as the default reflective loader, default shellcode stub, and default sleep mask.

To counter these types of defensive technologies, we have created the mutator kit. It makes use of LLVM-IR code to apply obfuscation passes to generate mutated object files. Hence, you can use the mutator kit to compile the sleep mask (`src*/sleepmask.c`) and completely break pre-canned YARA signatures. 

For more information on the mutator kit see the accompanying blog post: 
https://www.cobaltstrike.com/blog/introducing-the-mutator-kit-creating-object-file-monstrosities-with-sleep-mask-and-llvm

**Note:** The mutator kit only officially supports the sleep mask. This is because it is designed to break the use of in-memory YARA signatures **at scale** to detect Beacon when sleeping. You _can_ use it to compile other BOFs, however be warned that you will likely need to fix a number of compiler issues if you decide to do this (See the `Beacon Object Files` section below).

Additionally, it is important to use the following Malleable C2 settings:

```
stage {
    set sleep_mask "true";
    set cleanup "true"; # Instructs Beacon to clean up the initial memory allocation (of the raw Beacon DLL)
    set userwx "false"; # Instructs Beacon's loader to use RW/RX memory
}

process-inject {
    set startrwx "false"; # Instructs the sleep mask and BOFs to use RX memory for initial permissions
    set userwx "false"; # Instructs BOFs to avoid RWX for final permissions (NB doesn't impact sleep mask)
}
```

**Note:** `stage.userwx "true"` will instruct Beacon's loader to use RWX memory and cause the sleep mask to mask the .text section by default. `stage.userwx "false"` will instruct Beacon's loader to use RW/RX memory, and you will need to manually configure the sleep mask to mask the .text section. However, when `stage.userwx "false"` is set, the mutator kit will automatically enable `mask_text_section` for you to ensure the .text section is masked correctly. Starting with the Cobalt Strike 4.10 release the sleep mask will always mask the .text section and the `mask_text_section` is only used by previous versions of the sleep mask. We strongly recommend avoiding RWX memory wherever possible.

## Installation

The mutator kit can either be installed directly on an operator's workstation (this will be referred to as native) or installed inside a docker container. The installation process has been described below.

### Native

**Supported Distros:** Ubuntu 22.04

1. Execute `requirements.sh`.

This script will install the required dependencies and build the obfuscation plugin. It will also prompt you to set some required environment variables which you will need to do if you want to compile the sleep mask via the command line.

**Note:** On Windows endpoints this script must be installed using the Windows Subsystem for Linux (WSL) as Docker and LLVM on Windows can be quite complex. To install WSL (Ubuntu 22.04) see: https://learn.microsoft.com/en-us/windows/wsl/install. Additionally, if you have more than one WSL installation, make sure to set Ubuntu 22.04 as the default:
```
C:>wsl --list -v
NAME            STATE           VERSION

Ubuntu          Running         1
Ubuntu-22.04    Running         1

C:>wsl.exe --set-default Ubuntu-22.04
C:>wsl --list -v
NAME            STATE           VERSION

Ubuntu-22.04    Running         1
Ubuntu          Running         1
```

### Docker

**Supported Operating Systems:** Linux/macOS

(**NB Docker is the only way to run the mutator kit on macOS**)

To build and run the mutator kit with Docker :

1. Install docker - https://docs.docker.com/engine/install/.
2. Add your user to the `docker` group (`sudo usermod -aG docker $USER`) - https://docs.docker.com/engine/install/linux-postinstall/.
3. Execute `docker_mutator.sh`

**Note:** `docker_mutator.sh` will automatically build the mutator Docker image if it is not already present on the host. The script will also automatically mount the current working directory to the running docker container. This provides access to the input source files which makes it easier to copy them to your working directory for manual testing.

## Mutating the Sleep Mask

### Cobalt Strike Client

To start using the mutator kit:

1. Load `sleepmask_mutator.cna` in to the Script Manager.
2. Export a Beacon payload

**Note:** Navigate to `Sleep Mask Mutator -> Preferences` to customize how the sleep mask is generated and the obfuscation that is applied.  To use with previous Cobalt Strike versions modify the `$SLEEPMASK_VERSION` in the `sleepmask_mutator.cna` script to the appropriate directory and reload the script.

### Command Line

To manually compile sleep masks individually on the command line:
1. Execute `mutator.sh <target architecture> <clang args...>` (or `docker_mutator.sh` with the same arguments if using docker):
```
$ ./mutator.sh x64 -c -DMASK_TEXT_SECTION=1 -DIMPL_CHKSTK_MS=1 ../sleepmask/src/sleepmask.c -o sleepmask.x64.o
Obfuscation substitution enabled
Obfuscation flattening enabled
Obfuscation split-basic-blocks enabled
```
**Note:** The `-D` arguments above add an implicit `#define` to the target code and so can be used to specify configuration options for sleep mask (i.e. we're choosing to the mask the text section above). These options are the same defines used internally in the sleepmask `build.sh` script. Also note that the `-DIMPL_CHKSTK_MS=1` is needed when building the sleep mask with the mutator kit or else you will get linker errors.

### Additional Information

To dump the generated LLVM IR code, the following command can be used:
```
./mutator.sh x64 -emit-llvm -S -o example.ll example.c && cat example.ll
```
The `-S` flag instructs Clang to only run the preprocess and compilation steps. This can be useful as a quick way of checking whether the passes have been correctly applied (i.e. you can diff the outputted .ll file of the obfuscated code and compare it with the non-obfuscated version). For the full Clang command line reference see: https://clang.llvm.org/docs/ClangCommandLineReference.html.

To override the default obfuscation passes, you can pass in the `OBFUSCATIONS` environment variable:
```
OBFUSCATIONS=substitution,flattening ./mutator.sh ...
```
As a word of caution, the `bogus` option can dramatically increase the code size (which is expected as it introduces fake code paths). This can break the sleep mask size limit in Cobalt Strike and so is disabled by default.

**Note:** The mutator kit DOES NOT support the following built in sleep mask options:

- Any type of sys call
- Evasive sleep

This is by design as:
- Sys calls typically involve inline asm code blocks which cannot be mutated without breaking functionality. 
- The aim of this project is to break YARA signatures targeting the sleep mask in-memory and hence the evasive sleep mask is no longer necessary.

## Beacon Object Files (BOFs)

If you wanted to employ a high standard of OPSEC, you could also consider mutating other BOFs. The mutator in this repo can be used to compile BOFs, however bear in mind that the majority of open source BOFs are developed for use with different compilers (e.g. `x86_64-w64-mingw32-gcc`). Therefore, you will likely need to resolve a number of compiler/linker issues yourself in order to  successfully build them.

**Note:** Clang assumes some memory management functions, such as `memset` and `memcpy`, are provided. For example, Clang generates a call to `memset` when a big enough structure is initialized. `memory_funcs.c` provides a basic implementation for `memset` and `memcpy`, which can be used if you encounter object file parsing problems in Cobalt Strike with missing mem* functions.

## Further Reading

Below is a list of resources for developing your own LLVM passes if you wish to create your own tooling:

* https://llvm.org/docs/WritingAnLLVMNewPMPass.html
* https://llvm.org/docs/WritingAnLLVMPass.html
* https://github.com/quarkslab/llvm-passes/blob/master/doc/llvm_obfuscation_tutorial.rst
* https://polarply.medium.com/build-your-first-llvm-obfuscator-80d16583392b
* https://www.praetorian.com/blog/extending-llvm-for-code-obfuscation-part-1/
* https://0xpat.github.io/Malware_development_part_6/
* https://github.com/HikariObfuscator/Hikari/
* https://www.youtube.com/watch?v=iZMbGvhgNyU&pp=ygUPbGx2bSBvYmZ1c2NhdG9y
* https://medium.com/@mshockwave/writing-llvm-pass-in-2018-preface-6b90fa67ae82
* https://www.apriorit.com/dev-blog/687-reverse-engineering-llvm-obfuscation

## Common Docker Issues

- Some basic familiarity with Docker may be required. Please see: https://docker-curriculum.com/ for an overview of basic commands.
- If your Docker container appears to have no network connectivity see: https://stackoverflow.com/questions/53710206/docker-cant-build-because-of-alpine-error.
- If you modify `mutator.sh`, you will need to rebuild the Docker image. You can do this by deleting the existing image (`sudo docker images` / `sudo docker rmi <image_id>`) or by renaming the `IMAGE_NAME` in `docker_mutator.sh`.









---

# Mutator Kit

The Mutator Kit is the latest addition to the Cobalt Strike Arsenal, which is an LLVM obfuscator designed to break in-memory YARA scanning of the sleep mask.  If you're unfamiliar with what LLVM is, this "[LLVM in 100 Seconds](https://www.youtube.com/watch?v=BT2Cv-Tjq7Q)" video by Fireship provides a good overview.  Essentially, it's a compiler toolkit that can take the source code of any programming language and produce native executable machine code from it.  This is achieved by taking the raw source and running it through a lexer and parser to produce an intermediate representation (IR).  This is a low-level "reduced instruction set computer" (RISC) language, similar to assembly.  That IR can then be built as a static native object file for a supported CPU architecture.  LLVM already has lexers and parsers for many popular languages but you can also write your own.  This allows you to invent your own programming language and have LLVM compile it for you.  The LLVM project even has a [tutorial series](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html) on how to do that from scratch.

The Mutator Kit works by taking the source code of the sleep mask kit and parsing it into LLVM IR.  It then runs the IR through a number of obfuscation techniques before producing the final build.  This is a clever way of providing obfuscation without having to directly modify the original source code and each build of the sleep mask kit will be unique.

There are 4 types of obfuscation possible with the kit.  They are:

- **Substitution** - replace binary operators with functionally equivalent ones.  For example, replacing `a = b + c` with `a = b - (-c)` and other variations.
- **Control Flow Flattening & Basic-Block Splitting** - manipulates the control flow of a function by removing easily identifiable conditional and looping structures.
- **Bogus** - inserts fake control blocks to modify the control flow of a function.  It works by adding a conditional jump that points into either the original block or a fake block looping back to the conditional jump block.  This option is disabled in the kit by default because it can increase the final size of the compiled sleep mask.

Before using the Mutator Kit, ensure that your C2 profile is setup appropriately.  The recommended configurations are as follows:

```powershell
stage {
    set sleep_mask "true";
    set cleanup "true";
    set userwx "false";
}

process-inject {
    set startrwx "false";
    set userwx "false";
}
```

Payloads generated with this profile will have the default sleep mask applied, which will trigger the `Windows_Trojan_CobaltStrike_b54b94ac` YARA rule as it specifically targets the sleep obfuscation routine.

![](Attachments/yara-default.png)

Instead of building the sleep mask kit and loading sleepmask.cna as in the previous lesson, load `sleepmask_mutator.cna` from `C:\Tools\cobaltstrike\arsenal-kit\kits\mutator\`.  This will add a new Sleep Mask Mutator menu item which will launch a Preferences window.  These options can be left as they are.

![](Attachments/mutator.png)

Generate a new set of payloads using _Payloads > Windows Stageless Generate All Payloads_.  If you launch the Script Console, you will see the aggressor script calling into WSL to run the default sleep mask through the LLVM obfuscation.

```powershell
[sleepmask_mutator.cna] [+] BEACON_SLEEP_MASK hook invoked for LLVM mutated sleep mask
[sleepmask_mutator.cna] [*] Compiling an x64 LLVM mutated sleep mask...
[sleepmask_mutator.cna] wsl.exe --cd C:\Tools\cobaltstrike\arsenal-kit\kits -- CLANG=clang-14 LLVM_VERSION=14 LLVM_OBFUSCATOR_PATH=./mutator/libLLVMObfuscator.so OBFUSCATIONS=substitution,flattening,split-basic-blocks ./mutator/mutator.sh x64 -c -DIMPL_CHKSTK_MS=1 -DMASK_TEXT_SECTION=1 -o ./mutator/build/sleepmask.x64.o ./sleepmask/src49/sleepmask.c
[sleepmask_mutator.cna] C:\Tools\cobaltstrike\arsenal-kit\kits\mutator\build\sleepmask.x64.o length: 5041 bytes
[sleepmask_mutator.cna] [+] LLVM mutated sleep mask .text section SHA-256:
[sleepmask_mutator.cna] 412ee9b145471e91e772f0768a8ad827c2dbf3ff67626feedf92ce5c99b6f7ac
[sleepmask_mutator.cna] [+] Extracted LLVM mutated sleep mask bof length: 4665 bytes
```

The script prints the SHA256 checksum of the mask's `.text` section, `412ee9b145471e91e772f0768a8ad827c2dbf3ff67626feedf92ce5c99b6f7ac` in this example.  If you scan the entire output, you will see that every sleep mask has a different checksum.

Many of the previous YARA signatures are no longer present.

![](Attachments/yara-mutator.png)

One aspect to note about the Mutator Kit is that it is not compatible with evasive sleep or syscalls.  This is because syscalls involve inline assembly code that cannot be mutated without breaking functionality; and since the aim of this kit is to break YARA signatures targeting the sleep mask in-memory, the evasive sleep mask is no longer necessary.
