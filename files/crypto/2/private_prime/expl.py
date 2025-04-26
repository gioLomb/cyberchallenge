from Crypto.Util.number import long_to_bytes
import math

N = 7751526871113659666164486252578748649116909591277190089029732535127481176151524345597122598306249979629060800175410285871693995048150293635418099674432973398995520041393293777767941511445483996431026332997028403565850959357799371748394858804852228043653281960300204461432199938925289092169408545773233019123
Ciphertext = 4813784317490534191932457095527668318527989890720606628044645668719582196026497855453291519330699589742456932928170083183685945147596517298192372201753622124348955697985191325218715865125777867013838564483712717522945717927002788394921346947758322293598304497597954675810354257416529015463895970768411208028
e = 65537

# Cerchiamo k in un range ragionevole
for k in range(1, 100000):
    # Risolviamo l'equazione quadratica: k*p^2 + p - e*N = 0
    discriminant = 1 + 4 * k * e * N
    sqrt_discriminant = math.isqrt(discriminant)
    
    if sqrt_discriminant * sqrt_discriminant == discriminant:
        # Soluzione intera trovata
        p = (-1 + sqrt_discriminant) // (2 * k)
        if N % p == 0:
            q = N // p
            break

print(f"Found p: {p}")
print(f"Found q: {q}")

# Verifichiamo che q sia l'inverso di e mod p
assert (e * q) % p == 1

# Calcoliamo phi(N) = (p-1)*(q-1)
phi = (p - 1) * (q - 1)

# Calcoliamo la chiave privata d
d = pow(e, -1, phi)

# Decifriamo il ciphertext
plaintext = pow(Ciphertext, d, N)
flag = long_to_bytes(plaintext)

print(f"Flag: {flag.decode()}")