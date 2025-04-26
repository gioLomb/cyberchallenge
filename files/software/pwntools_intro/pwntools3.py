from pwn import *

p_elf = process('./sw-19')

p = remote('software-19.challs.olicyber.it', 13002)
elf = ELF('./sw-19')

p.recvuntil(b'iniziare')
p.sendline(b'p')

while True:
    lines = p.recv().decode('utf-8').splitlines()
    print('linee',lines)
    for line in lines:
        if '->' in line:
            elements = line.split()
            symbol = elements[1].replace(':', '')
            print(f"Simbolo richiesto: {symbol}")
            
            # Ottieni l'indirizzo dall'ELF
            addr = elf.sym[symbol]
            p.sendline(str(hex(addr)).encode())
            
           
