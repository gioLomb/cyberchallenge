from pwn import *

p = remote('piecewise.challs.cyberchallenge.it', 9110)

while True:
    try:
        # Ricevi i dati dal server
        data = p.recv(timeout=5)
        if not data:
            break  # Se non riceve nulla, esce dal ciclo

        # Stampa tutto il messaggio ricevuto per debugging
        print("📥 Messaggio ricevuto:\n", data.decode(errors='ignore'))

        # Dividiamo il messaggio in righe per gestire separatamente flag e richieste
        lines = data.splitlines()

        for line in lines:
            if b"Partial flag" in line:
                print("🚩 Parte della flag:", line.decode(errors='ignore'))
                continue

            if b"Please send me an empty line" in line:
                print("⚡ Richiesta di riga vuota, invio `\\n`...")
                p.send(b"\n")  # Invia solo un newline
                continue

            if b"Please send me the number" in line:
                splitted = line.split(b" ")

                if len(splitted) < 10:
                    print("⚠️ Messaggio non nel formato atteso, salto...")
                    continue

                # Estraggo i dati necessari
                num = int(splitted[5].decode('utf-8'))  # Numero da inviare
                arch = splitted[8]  # Architettura (32-bit o 64-bit)
                endian = (splitted[9].split(b'-')[0]).decode('utf-8')  # Endianness

                print(f"📝 Numero: {num}, Architettura: {arch.decode()}, Endian: {endian}")

                # Invia il numero nel formato corretto SENZA \n
                if arch == b'32-bit':
                    p.send(p32(num, endian=endian))
                elif arch == b'64-bit':
                    p.send(p64(num, endian=endian))

                print("✅ Risposta inviata!")

    except Exception as e:
        print(f"❌ Errore: {e}")
        break

p.interactive()
