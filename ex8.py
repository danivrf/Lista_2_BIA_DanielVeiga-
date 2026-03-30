def inventario_equipamentos():
    n = int(input("Quantos equipamentos deseja cadastrar? "))

    nomes = []
    valores = []

    total = 0

    for i in range(n):
        nome = input(f"Digite o nome do equipamento {i+1}: ")
        valor = float(input(f"Digite o valor do equipamento {i+1}: "))

        nomes.append(nome)
        valores.append(valor)

        total += valor

   
    mais_caro = valores[0]
    mais_barato = valores[0]
    nome_caro = nomes[0]
    nome_barato = nomes[0]

    
    for i in range(n):
        if valores[i] > mais_caro:
            mais_caro = valores[i]
            nome_caro = nomes[i]

        if valores[i] < mais_barato:
            mais_barato = valores[i]
            nome_barato = nomes[i]

    
    print("\nLista de equipamentos:")
    for i in range(n):
        print(f"{nomes[i]} - R$ {valores[i]:.2f}")

    print(f"\nValor total do inventário: R$ {total:.2f}")
    print(f"Mais caro: {nome_caro} - R$ {mais_caro:.2f}")
    print(f"Mais barato: {nome_barato} - R$ {mais_barato:.2f}")


inventario_equipamentos()