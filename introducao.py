import statistics as es

historia_n1 = float(input('Digite a primeira nota '))
historia_n2 = float(input('Digite a segunda nota '))

lista_notas = [historia_n1, historia_n2]

soma = sum(lista_notas)
media = es.mean(lista_notas)

if media >= 7:
    print('aprovado')

elif media >= 5 and media < 7:
    print('Recuperação')

else:
    print('REPROVADO')