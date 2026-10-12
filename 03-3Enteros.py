a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))
c = int(input("Tercer numero: "))

if a > b:
    if a > c:
        print(f"{a} es mayor")
    else:
        print(f"{c} es mayor")
else:
    if b > c:
        print(f"{b} es mayor")
    else:
        print(f"{c} es mayor")