num = int(input('Forneça um numero qualquer: '))

cont = 1
soma = 0

while cont <= num:
    print(cont)
    soma += cont
    cont += 1

print(f'Soma total = {soma}')