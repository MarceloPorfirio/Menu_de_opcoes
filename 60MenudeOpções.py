from time import sleep
num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao !=5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior número
    [ 4 ] Novos números
    [ 5 ] Sair ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        res = num1 + num2
        print('A soma entre {} e {} é = {}'.format(num1,num2,res))
    elif opcao ==2:
        res = num1 * num2
        print('A multiplicação entre {} e {} é = {}'.format(num1,num2,res))
    elif opcao == 3:
        if num1 > num2:
            print('O {} é maior que o {}.'.format(num1,num2))
        else:
            print('O {} é maior que o {}.'.format(num2,num1))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        num1 = int(input('Primeiro Valor: '))
        num2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida! Digite novamente!')
    sleep(2)
print('Fim do programa!')
