
the code starts by openning the root file next comes a call to mmap to create a new mapped memeory segment in the new memory process, one of the parameters that mmap takes is a file descriptor with attribute read only. this means it maps the file into a new memory area, the permission flags on the memory area also show that theyre read only 

the other important flag is the map private flag, the comment here is coppied from the man page and this create a private copy on write mapping... for short C.O.W, it doesnt copy the whole content of the file into memory it maps the file into your memory, this is usually sick since you dont need huge amounts of ram to copy the file into memory,  you just fdirectly read from the file on disk. we will read more about memory in a second

copy on write means that if you were to write to the memory segment you would then create a copy of it, so even though the file is mapped as read only because of the private mapping we can write to a COPY of it.

the next step is starting 2 threads that start in parallel, its a race condition vulnerability this means certain events have to occur in a special order that are fairly unlikely to happen under normal circumstances so you need to increase the probability 

what the 2 threads are doing?

one of them is using madvise, its using the syscal madvise but it stands for MADadvise, this syscall is used for optimization reasons you can provide the kernel with some information as to how you want to intend to use a memory mapped area because there are different techniques in handling caching 

one advise we gave to the kernel is that we dont need advise for the first 100 bytes 



the second thread opens a proc/sef/mem  opens the file proc/self/mem which is a very special file to put the least so proc is a so called sudo file system

/proc is information about processes

/proc/self/ current process

inside of this is the mem "file" which is a representation of the current processes memory.

in this case the exploit writes to the file in a loop first it performs a seek which moves the cursor to the start of the file that we mapped into memory  and then it writes the string we pass via program arguments to it, so this will trigger a copy of the memory so that we can write to it so that we can see the changes. remember we wont write to the REAL file so if you would do these things once or isolated from one another thats file, but because theres a race condition issue somewhere, repeating this over and over will create a weird edge case where we actually end up tricking the kernel and writing to the underlying file 

now lets look at the patch

the file that was patched belongs to the linux memory manager hence the MM directory and the file itself is called gpu which stands for get_user_pages 

when we c





https://chao-tic.github.io/blog/2017/05/24/dirty-cow