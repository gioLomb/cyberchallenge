
m1 = '158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf'
m2 = '73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2'
m1 =bytes.fromhex(m1)
m2=bytes.fromhex(m2)
res=[]
for i in range(0,len(m1)):
    res.append(m1[i] ^ m2[i])

print(bytes(res))