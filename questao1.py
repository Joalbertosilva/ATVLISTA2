n1 = 0
n2 = 1
nf = 0

for i in range(0, 14):
    nf = n1 + n2
    n1 = n2
    n2 = nf
    print(nf)