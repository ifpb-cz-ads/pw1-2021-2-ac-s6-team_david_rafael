num1 = int(input('Dividendo: '))
num2 = int(input('Divisor: '))
x = num1
resto = 0
cont = 0

while x >= num2:
    x = x - num2
    cont = cont + 1

resto = x

print('{} / {} é {} resto = {}'.format(num1, num2, cont, resto))