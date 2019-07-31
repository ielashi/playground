A fancier boot sector that types a fancy text.

I did this to refresh my memory on writing functions in assembly.

To run:
```
nasm -f bin fancy.asm -o fancy.bin
```

```
qemu-system-x86_64 -drive format=raw,file=fancy.bin
```


![Output](https://github.com/ielashi/playground/blob/master/bootsector-hello-world-fancy/output.png)
