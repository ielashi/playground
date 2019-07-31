mov ah, 0x0e  ; Adding a pointer to the BIOS routine for printing a character in the a register.

mov al, 'H'   ; Adding the argument to the BIOS routine (the character) in the lower bits.
int 0x10      ; Raise an interrupt for the BIOS routine to run
mov al, 'e'
int 0x10
mov al, 'l'
int 0x10
int 0x10
mov al, 'o'
int 0x10

jmp $         ; Infinite loop, we the terminal halts foever.

times 510-($-$$) db 0  ; Padd rest of sector with zeros.
dw 0xaa55     ; Add magic word for BIOS to know this is a boot block.
