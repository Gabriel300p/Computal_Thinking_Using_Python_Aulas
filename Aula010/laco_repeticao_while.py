contador_par = 2
contador_impar = 1
soma_par = 0
soma_impar = 0
media = 25

print("--- Caro(a) Professor(a), entre com as notas dos alunos ---")
while contador_impar <= 5:
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO: ", contador_impar)
    nota = float(input("--> "))
    contador_impar += 2
    soma_impar += nota

    while nota < 0 or nota > 10:
        print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO: ", contador_impar)
        nota = float(input("Nota Inválida! Digite novamente!"))
        contador_impar += 2
        soma_impar += nota

while contador_par <= 6:
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO: ", contador_par)
    nota = float(input("--> "))
    soma_par += nota
    contador_par += 2

    while nota < 0 or nota > 10:
        print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES. POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO: ", contador_par)
        
        nota = float(input("Nota Inválida! Digite novamente!"))
        soma_par += nota
        contador_par += 2

media_par = soma_par / media
media_impar = soma_impar / media
print("Média dos alunos PARES: {:.1f}" .format(media_par))
print("Média dos alunos ÍMPARES: {:.1f}" .format(media_impar))
print("A turma que teve maior nota foi a: ")
if media_par > media_impar:
    print("PAR")
elif media_impar > media_par:
    print("IMPAR")
else:
    print("As duas turmas (pares e ímpares) tiveram a mesma média")


print("Finalizou!")
