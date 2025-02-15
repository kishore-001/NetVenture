section .text
global _start
_start:
    ; Display password prompt
    mov eax, 4          ; syscall write
    mov ebx, 1          ; stdout
    mov ecx, prompt     ; prompt message
    mov edx, prompt_len ; length of prompt
    int 0x80

    ; Read user input
    mov eax, 3          ; syscall read
    mov ebx, 0          ; stdin
    mov ecx, user_input
    mov edx, 10         ; Read up to 10 bytes
    int 0x80

    ; Remove newline character
    mov esi, user_input
trim_loop:
    cmp byte [esi], 0x0A
    je replace_null
    cmp byte [esi], 0
    je compare_input
    inc esi
    jmp trim_loop

replace_null:
    mov byte [esi], 0

compare_input:
    ; Compare input with password "movAL"
    mov esi, user_input
    mov edi, correct_password
    mov ecx, 6          ; Password length + null terminator
compare_loop:
    mov al, [esi]
    cmp al, [edi]
    jne fail
    inc esi
    inc edi
    loop compare_loop

success:
    ; Construct flag at runtime
    mov edi, constructed_flag
    
    ; MAGNUS{
    mov byte [edi], 77     ; M
    inc edi
    mov byte [edi], 65     ; A
    inc edi
    mov byte [edi], 71     ; G
    inc edi
    mov byte [edi], 78     ; N
    inc edi
    mov byte [edi], 85     ; U
    inc edi
    mov byte [edi], 83     ; S
    inc edi
    mov byte [edi], 123    ; {
    inc edi
    
    ; Rev_
    mov byte [edi], 82     ; R
    inc edi
    mov byte [edi], 101    ; e
    inc edi
    mov byte [edi], 118    ; v
    inc edi
    mov byte [edi], 95     ; _
    inc edi
    
    ; Eng_
    mov byte [edi], 69     ; E
    inc edi
    mov byte [edi], 110    ; n
    inc edi
    mov byte [edi], 103    ; g
    inc edi
    mov byte [edi], 95     ; _
    inc edi
    
    ; Asm_
    mov byte [edi], 65     ; A
    inc edi
    mov byte [edi], 115    ; s
    inc edi
    mov byte [edi], 109    ; m
    inc edi
    mov byte [edi], 95     ; _
    inc edi
    
    ; Challenge}
    mov byte [edi], 67     ; C
    inc edi
    mov byte [edi], 104    ; h
    inc edi
    mov byte [edi], 97     ; a
    inc edi
    mov byte [edi], 108    ; l
    inc edi
    mov byte [edi], 108    ; l
    inc edi
    mov byte [edi], 101    ; e
    inc edi
    mov byte [edi], 110    ; n
    inc edi
    mov byte [edi], 103    ; g
    inc edi
    mov byte [edi], 101    ; e
    inc edi
    mov byte [edi], 125    ; }
    inc edi
    mov byte [edi], 10     ; newline
    
    ; Display constructed flag
    mov eax, 4
    mov ebx, 1
    mov ecx, constructed_flag
    mov edx, flag_len
    int 0x80
    jmp exit

fail:
    mov eax, 4
    mov ebx, 1
    mov ecx, msg_fail
    mov edx, fail_len
    int 0x80

exit:
    mov eax, 1
    xor ebx, ebx
    int 0x80

section .data
prompt db "Enter password: "    ; New prompt message
prompt_len equ $ - prompt      ; Length of prompt
msg_fail db "Incorrect password!", 10
fail_len equ $ - msg_fail
correct_password db "__bss_start!", 0
flag_len equ 30                ; Length of complete flag + newline

section .bss
user_input resb 10
constructed_flag resb 30       ; Buffer for constructing the flag