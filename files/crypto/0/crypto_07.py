from Crypto.Cipher import DES,AES,ChaCha20
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from pwn import *
p=remote('crypto-07.challs.olicyber.it' ,30000)
# Chiave in esadecimale da convertire in bytes (DES richiede 8 byte)
key = bytes.fromhex('552be90c49f59fe2')

# IV di 8 byte (puoi generarlo casualmente o definirlo fisso per test ripetibili)
iv = get_random_bytes(8)
print('iv: ',iv.hex())
# Testo da cifrare (in bytes)
plaintext = "La lunghezza di questa frase non è divisibile per 8".encode('UTF-8')

# Padding usando X.923
padded_pltxt = pad(plaintext, DES.block_size, style='x923')

# Crea l'oggetto cifrario in modalità CBC con chiave e IV
cipher = DES.new(key, DES.MODE_CBC, iv)

# Cifra il testo
ciphertext = cipher.encrypt(padded_pltxt)
print("Ciphertext (hex):", ciphertext.hex())
# Send the ciphertext
print(p.recv())
p.recvuntil('?')
p.sendline(ciphertext)  # Directly send the ciphertext bytes without waiting for a prompt

# Send the IV as bytes (without using `sendlineafter`)
p.sendline(bytes.fromhex(iv.hex())) 


#p.recvuntil('?')

#p.sendline('jnjhjj')
#p.interactive()
