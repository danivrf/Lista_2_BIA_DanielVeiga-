def tabuada():
    num = int(input('Digite um número: '))

    intervalo = int(input('Digite ate qual numero voce deseja que a tabuada seja feita: '))
    
    for n in range(intervalo + 1):
        resultado = num * n
        print(f'{num} x {n} = {resultado}')
        
        
tabuada()
