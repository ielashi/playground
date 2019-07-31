print_string:
  pusha  ; push all registers onto the stack.
  mov ah, 0x0e ; we'll be calling the BIOS routine for printing a character

print_char:
  mov al, [bx]    ; load the character in the a register

  cmp al, 0       ; if we reached the end of the string, exit
  je print_string_end

  int 0x10      ; raise an interrupt for it to be called
  add bx, 0x01
  jmp print_char

print_string_end:
  popa   ; restore all registers.
  ret

