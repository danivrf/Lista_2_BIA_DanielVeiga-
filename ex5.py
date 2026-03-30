def calculo_temperatura():
    temperaturas = []

    for n in range(1, 8):
        temp = float(input(f'Digite a temperatura {n} em °C: '))
        temperaturas.append(temp)

    soma = 0
    maior = temperaturas[0]
    menor = temperaturas[0]
    dia_maior = 1
    dia_menor = 1

    for i in range(len(temperaturas)):
        soma += temperaturas[i]

        if temperaturas[i] > maior:
            maior = temperaturas[i]
            dia_maior = i + 1

        if temperaturas[i] < menor:
            menor = temperaturas[i]
            dia_menor = i + 1

    media = soma / len(temperaturas)

    
    print(f'Média das temperaturas: {media:.2f} °C')
    print(f'Maior temperatura: {maior} °C no dia {dia_maior}')
    print(f'Menor temperatura: {menor} °C no dia {dia_menor}')


calculo_temperatura()