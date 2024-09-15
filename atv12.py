# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.
nota=float(input("Qual a sua primeira nota:"))
nota2=float(input("Qual a sua segunda nota:"))
media = (nota + nota2)/2
if media>=7:
    print("Aprovado")
else:
    print("Reprovado")