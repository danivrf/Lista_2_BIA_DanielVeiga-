def analisar_notas():
    nota = float(input("Digite uma nota (-1 para encerrar): "))

    if nota == -1:
        print("Nenhuma nota inserida")
    else:
        maior = nota
        menor = nota
        soma = 0
        quantidade = 0
        notas = []

        while nota != -1:
            soma += nota
            quantidade += 1
            notas.append(nota)

            if nota > maior:
                maior = nota

            if nota < menor:
                menor = nota

            nota = float(input("Digite uma nota (-1 para encerrar): "))

        media = soma / quantidade

        acima_media = 0
        for n in notas:
            if n > media:
                acima_media += 1

    
        print("Quantidade de notas:", quantidade)
        print("Média:", media)
        print("Maior nota:", maior)
        print("Menor nota:", menor)
        print("Notas acima da média:", acima_media)


analisar_notas()