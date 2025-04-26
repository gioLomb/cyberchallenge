from pwn import *
p=remote('software-18.challs.olicyber.it',13001)
p.recvuntil('iniziare')
p.sendline(b'b')
while(True):
    lines=p.recv(timeout=5).decode('utf-8').splitlines()
    print('tutte le linee',lines)
    for line in lines:
        if 'restituiscimi' in line:
            elements=line.split()
            print('LINEA',elements)
            print('numero',elements[5])
            numero=int(elements[5],16)
            print(numero)
            bit=int(elements[8].split('-')[0])
            print(bit)
            if bit==64:
                print('ig',64)
                p.send(p64(numero,bit))
            elif bit==32:
                print('ik',32)
                p.send(p32(numero,bit))
            break


```
from pwn import *
import ast

HOST = "software-18.challs.olicys<dber.it"
PORT = 13001
r = remote(HOST, PORT)
r.recv(1024)
r.send(b'a\r\n')

for i in range(100):
    stringa = r.recvline().decode().split(' ')
    numero = stringa[5]
    numero_int = int(numero, 16)
    packed = stringa[6]
    bit = stringa[8].split('-')[0]
    out = ""
    
    if(bit == "16"):
        if(packed  == "packed"):
            out = p16(numero_int, endianness="little")
        else:
            out = u16(str(numero), endianness="little")
    if (bit == "32"):
        if(packed  == "packed"):
            out = p32(numero_int, endianness="little")
        else:
            out = u32(str(numero), endianness="little")
    if (bit == "64"):
        if(packed  == "packed"):
            out = p64(numero_int, endianness="little")
        else:
            out = u64(str(numero), endianness="little")

    print(out)
    print(r.recv(1024))
    r.send(str(out) + '\r\n')
    print(r.recv(1024))

print(r.recv(1024))
```

    
    



