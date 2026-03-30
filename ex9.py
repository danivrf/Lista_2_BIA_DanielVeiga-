def simulacao_investimento():
    capital = float(input("Digite o capital inicial: "))
    taxa = float(input("Digite a taxa de juros mensal (%): "))
    alvo = float(input("Digite o valor alvo: "))

    taxa = taxa / 100 

    montante = capital
    meses = 0
    juros_total = 0

    print("\nExtrato:")

    while montante < alvo:
        rendimento = montante * taxa
        montante += rendimento
        juros_total += rendimento
        meses += 1

        print(f"Mês {meses}: rendimento = R$ {rendimento:.2f} ----- montante = R$ {montante:.2f}")

    print("\nResumo:")
    print(f"Meses necessários: {meses}")
    print(f"Montante final: R$ {montante:.2f}")
    print(f"Total de juros: R$ {juros_total:.2f}")


simulacao_investimento()