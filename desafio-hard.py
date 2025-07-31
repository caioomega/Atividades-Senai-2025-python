acertos = 0
erros = 0
while True:
    num = int(input('Digite um número para treinar a tabuada: '))
    for i in range (1, 11):
        print (f'{num} x {i} = ? ')
        resposta = int (input ('Resposta: '))
        
        if resposta == num * i:
            print ("certo!!")
            acertos += 1
        else:
            print (f'errado!! o resultado correto é {num * i}')
            erros += 1
            print(f'acertos: {acertos} erros: {erros}')
            cont = input ('deseja treinar outro numero? s/n')
            if cont == 'n':
                break
            