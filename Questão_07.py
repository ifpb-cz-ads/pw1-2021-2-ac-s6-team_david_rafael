primeiro= int(input("Digite o primeiro numero:"))
segundo= int(input("Digite o segundo numero:"))
x=1
y=0
while x <= segundo:
    y = y + primeiro
    x = x + 1
print(f"{primeiro} x {segundo} = {y}")