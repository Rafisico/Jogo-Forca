import random

list=''
secreto='peruca'
digitadas=[]
chances = 15
x=0



while chances <=10:
    print(f'Você possui {chances} chances.')
    print()
    letra=input('Digite uma letra: ')

    if len(letra)>1:
        print('Digite apenas uma letra')
        continue


    digitadas.append(letra)

    if letra in secreto:
        print(f'Boa! a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Puts, a letra "{letra}" não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'A palavra secreta é: {secreto}')
        print('PARABÉNS, VOCÊ VENCEU!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    print()

    chances-=1
else:
    print('Você perdeu!')