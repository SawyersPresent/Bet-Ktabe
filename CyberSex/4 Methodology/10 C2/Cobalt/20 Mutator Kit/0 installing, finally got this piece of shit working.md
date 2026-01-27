

Dockerfile, the problem here was the alpine verison, it was just 3 and it shouldve been 3.19

```python
ARG LLVM_VERSION=14                                                                                                                                                                                                
                                                                                                                                                                                                                   
# Build stage
FROM alpine:3.19 AS build
ARG LLVM_VERSION

WORKDIR /

# Install build dependencies
RUN apk update && apk --no-cache add \
    llvm$LLVM_VERSION-static \
    llvm$LLVM_VERSION-dev \
    git \
    g++ \
    make \
    cmake \
    libxml2-dev

# Build the obfuscator LLVM plugin
RUN git clone --depth 1 --branch 20240115 --single-branch https://github.com/Cobalt-Strike/obfuscator-llvm.git \
    && mkdir obfuscator-llvm/build \
    && cd obfuscator-llvm/build \
    && cmake -DLLVM_DIR=/usr/lib/llvm$LLVM_VERSION/lib/cmake .. \
    && make

# Run stage
FROM alpine:3.19 AS mutator
ARG LLVM_VERSION
ARG OBFUSCATOR_PATH=/obfuscator.so

# Install run dependencies
RUN apk update && apk --no-cache add \
    llvm$LLVM_VERSION \
    clang$LLVM_VERSION \
    mingw-w64-headers \
    i686-mingw-w64-headers

# Copy the compiled plugin from the build stage
COPY --from=build /obfuscator-llvm/build/libLLVMObfuscator.so $OBFUSCATOR_PATH

# Copy our entrypoint
COPY --chmod=755 mutator.sh /entrypoint.sh

# Set up the environment
WORKDIR /src
ENV LLVM_VERSION=$LLVM_VERSION
ENV LLVM_OBFUSCATOR_PATH=$OBFUSCATOR_PATH
ENV OBFUSCATIONS="flattening,substitution,split-basic-blocks"

ENTRYPOINT ["/entrypoint.sh"]

```



mutator.sh

```python
#!/bin/sh
# Usage: mutator.sh <target> <clang args>
#     - target: Set the target architecture type, and select the correct Windows headers.
#               Possible values: x64, x86.
#     - clang args: Passed arguments to clang
#
# Required environment variables:
#     - CLANG = Clang binary path
#     - LLVM_OBFUSCATOR_PATH = Obfuscator plugin path
#     - OBFUSCATIONS = Comma-separated list of selected mutations.
#                      Supported values: flattening, bogus, substitution, split-basic-blocks
#
# Example usage: $ CLANG=clang-14 \
#                  LLVM_OBFUSCATOR_PATH=obfuscator.so \
#                  OBFUSCATIONS=substitution,flattening \
#                  ./mutator.sh x64 -c hello.c -o hello.x64.o
set -o errexit
set -o nounset

[ -z "$*" ] && echo "Usage: mutator.sh <x64|x86> <clang args>" && exit 0

# Set compiler flags based on the selected target (the first argument)
case "$1" in
    x64)
        shift
        TARGET_FLAGS="-I/usr/x86_64-w64-mingw32/include -target x86_64-w64-mingw32" \
    ;;
    x86)
        shift
        TARGET_FLAGS="-I/usr/i686-w64-mingw32/include -target i686-w64-mingw32" \
    ;;
    *)
        TARGET_FLAGS="" \
    ;;
esac

# Execute clang with the obfuscator plugin and the selected mutations
CLANG=${CLANG:-"clang-$LLVM_VERSION"}
LLVM_OBF_SCALAROPTIMIZERLATE_PASSES=$OBFUSCATIONS \
    "$CLANG" \
    -fno-legacy-pass-manager \
    "-fpass-plugin=$LLVM_OBFUSCATOR_PATH" \
    $TARGET_FLAGS \
    "$@"

```



```
kali@kali ~/c/a/k/mutator> sudo ./docker_mutator.sh
The mutator:latest not exists, building the image...
[+] Building 204.9s (12/12) FINISHED                                                                                                                                                                docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                                          0.1s
 => => transferring dockerfile: 1.27kB                                                                                                                                                                        0.0s 
 => [internal] load metadata for docker.io/library/alpine:3.19                                                                                                                                                0.0s 
 => [internal] load .dockerignore                                                                                                                                                                             0.0s 
 => => transferring context: 2B                                                                                                                                                                               0.0s 
 => [internal] load build context                                                                                                                                                                             0.0s 
 => => transferring context: 1.51kB                                                                                                                                                                           0.0s 
 => [build 1/4] FROM docker.io/library/alpine:3.19                                                                                                                                                            0.0s 
 => [build 2/4] RUN apk update && apk --no-cache add     llvm14-static     llvm14-dev     git     g++     make     cmake     libxml2-dev                                                                    186.3s 
 => [mutator 2/5] RUN apk update && apk --no-cache add     llvm14     clang14     mingw-w64-headers     i686-mingw-w64-headers                                                                              179.0s
 => [build 3/4] RUN git clone --depth 1 --branch 20240115 --single-branch https://github.com/Cobalt-Strike/obfuscator-llvm.git     && mkdir obfuscator-llvm/build     && cd obfuscator-llvm/build     && cm  15.9s 
 => [mutator 3/5] COPY --from=build /obfuscator-llvm/build/libLLVMObfuscator.so /obfuscator.so                                                                                                                0.0s 
 => [mutator 4/5] COPY --chmod=755 mutator.sh /entrypoint.sh                                                                                                                                                  0.0s 
 => [mutator 5/5] WORKDIR /src                                                                                                                                                                                0.0s 
 => exporting to image                                                                                                                                                                                        2.5s 
 => => exporting layers                                                                                                                                                                                       2.5s 
 => => writing image sha256:f93195ab69ea11e12679d3341dbf3060cfeda19b121d7372286b5373b15f8629                                                                                                                  0.0s 
 => => naming to docker.io/library/mutator:latest                                                                                                                                                             0.0s 
Usage: mutator.sh <x64|x86> <clang args>                                                                                                                                                                           
```