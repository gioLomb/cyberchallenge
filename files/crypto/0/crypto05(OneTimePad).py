ciphertext_hex = "104e137f425954137f74107f525511457f5468134d7f146c4c"
ciphertext = bytes.fromhex(ciphertext_hex)

for k in range(256):
    # Decifra: XOR di ogni byte con la chiave k
    plaintext = "".join(chr(b ^ k) for b in ciphertext)
    print(plaintext)
#provo 256 valori perchè la chiave è lunga 1 byte quindi
#con un valore della chiave riesco a decifrare tutti i char
# del cyphertext dopo averlo codificati in ascii

    
   
