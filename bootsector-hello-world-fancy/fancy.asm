[org 0x7c00] ; The address where the code will be loaded.

mov bx, HELLO_MSG
call print_string

jmp $ ; hang

%include "print_string.asm"

HELLO_MSG:
  db "  _                 _         ____   _____", `\n`, 0x0d
  db " (_)               | |       / __ \ / ____|", `\n`, 0x0d
  db "  _ _ __ ___   __ _| | _____| |  | | (___", `\n`, 0x0d
  db " | | '_ ` _ \ / _` | |/ / _ \ |  | |\___ \", `\n`, 0x0d
  db " | | | | | | | (_| |   <  __/ |__| |____) |", `\n`, 0x0d
  db " |_|_| |_| |_|\__,_|_|\_\___|\____/|_____/", `\n`, 0x0d



times 510 - ($-$$) db 0
dw 0xaa55
