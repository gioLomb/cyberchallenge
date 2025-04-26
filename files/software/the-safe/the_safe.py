from pwn import *

p=process('./the_safe')
p.interactive()
p.sendline('you_cAnT_gue55_th1z_s3cur3_p@ssword')

