message="This is plaintext"
p=4173306299
q=2262123937

n=p*q
print((p-1)*(q-1))
print(n)
e=1
ris=''
for c in message:
    ris+=str(pow(ord(c),e,n))
print(ris)

                             s_you_cAnT_gue55_th1z_s3cur3_p@ssw_0804a084     XREF[2]:     main:080493e5(*), 
                                                                                          main:080493eb(*)  
        0804a084 79 6f 75        ds         "you_cAnT_gue55_th1z_s3cur3_p@ssword"
                 5f 63 41 
                 6e 54 5f 
