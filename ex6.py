def numeros_primos():

    num = int(input('Digite um numero: '))
    quant = 0

    for n in range(2, num + 1):
        divisores = 0
        for i in range(1, n + 1):
            if n % i == 0:
                divisores += 1
        if divisores == 2:  
            print(n)
            quant += 1

    print("Quantidade de números primos:", quant)

numeros_primos()