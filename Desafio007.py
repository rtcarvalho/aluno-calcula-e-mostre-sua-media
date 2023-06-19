print('Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media: ')
nome = str(input('Digite seu nome: '))
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

soma = (nota1+nota2) / 2

print("Media: {:.1f}" .format(soma))

if soma >= 7:
    print('Parabens {}! você foi Aprovado!' .format(nome))

else:
    print('Poxa {}! Infelizmesnte você foi Reprovado' .format(nome))