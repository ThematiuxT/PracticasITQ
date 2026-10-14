import math
n = int(input("Introduce numero: "))
primo = True
for i in range(2,math.ceil(math.sqrt(n))+1,1):
    if n == 2:
        break
    if n % i == 0:
        primo = False
        break

if primo:
    print("Es primo.")
else:
    print("No es primo")