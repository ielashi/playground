Building a bootsector in x86 assembly that prints hello.

To run:
```
nasm -f bin hello.asm -o hello.bin
```
```
qemu-system-x86_64 -drive format=raw,file=hello.bin
```

![Output](https://github.com/ielashi/playground/blob/master/bootload-hello-world/output.png)
