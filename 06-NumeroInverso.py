st = str(int(input("Numero: ")))
n = 0
for i in range(len(st)):
    n = n + (int(st[i])*(10**i))
print(n)