from pwn import *

p=remote('software-17.challs.olicyber.it',13000)

p.sendline(b'p')
while(True):
    comando=p.recvuntil(b'\n[')
    numeri=p.recvuntil(b']\n',True)
    #print(numeri)
    numeri=numeri.decode('utf-8').split(', ')
    somma=0
    for num in numeri:
        somma+=int(num)
    p.sendline(str(somma).encode())
    #print(bytes(somma))
    print(comando)
    if b'Step 10' in comando:
        while(True):
            comando=p.recvline()
            print(comando)
    #p.interactive()




