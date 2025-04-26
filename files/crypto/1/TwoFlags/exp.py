from PIL import Image
import numpy as np

# Carica le immagini cifrate
enc1 = Image.open("/home/kali/Desktop/cc/files/crypto/1/TwoFlags/flag_enc.png")
enc2 = Image.open("/home/kali/Desktop/cc/files/crypto/1/TwoFlags/notflag_enc.png")

# Converti in array NumPy
enc1_np = np.array(enc1)
enc2_np = np.array(enc2)

# Esegui XOR tra le due immagini cifrate
diff = np.bitwise_xor(enc1_np, enc2_np)

# Salva il risultato
Image.fromarray(diff).save("diff.png")

print("[+] Salvata differenza visuale in 'diff.png'")
print("[*] È la XOR tra flag.png e notflag.png")
