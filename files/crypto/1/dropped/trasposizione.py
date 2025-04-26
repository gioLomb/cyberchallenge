# Funzione per il cifrario a colonne
def columnar_transposition_encrypt(plaintext, key):
    # Creiamo una lista di colonne
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols + (1 if len(plaintext) % num_cols != 0 else 0)
    
    # Riempiamo le colonne
    grid = ['' for _ in range(num_cols)]
    for i, char in enumerate(plaintext):
        grid[i % num_cols] += char

    # Ora possiamo ottenere la stringa cifrata
    cipher_text = ''.join(grid)
    return cipher_text

# Funzione per Rail Fence
def rail_fence_encrypt(plaintext, num_rails):
    # Creiamo un array vuoto per immagazzinare le righe
    rails = ['' for _ in range(num_rails)]
    direction = 1  # 1 significa andare verso il basso, -1 verso l'alto
    rail = 0  # Iniziamo dalla prima riga
    for char in plaintext:
        rails[rail] += char
        # Cambiamo riga seguendo il pattern
        if rail == 0 or rail == num_rails - 1:
            direction = -direction
        rail += direction

    # Leggiamo i caratteri per riga
    return ''.join(rails)

# Test con il messaggio dato: "TCICmI_{_d343_m4}s!s"
plaintext = "TCICmI_{_d343_m4}s!s"

# Proviamo con il cifrario a colonne
key = "KEY"  # Chave da testare (può essere variata)
columnar_result = columnar_transposition_encrypt(plaintext, key)

# Proviamo con il cifrario Rail Fence
rail_fence_result = rail_fence_encrypt(plaintext, 3)  # con 3 righe

columnar_result, rail_fence_result
