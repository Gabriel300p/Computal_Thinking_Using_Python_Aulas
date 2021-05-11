'''
1) A prefeitura de Recife criou um programa de empréstimo para seus funcionários com desconto em folha. O valor da prestação não pode ultrapassar 30% do salário bruto do funcionário. Faça um programa em Python que solicite o valor do salário bruto, o valor da prestação e informe se o empréstimo pode ou não ser concedido.
Validações: Não aceitar salário 
<=0 Não aceitar prestação <=0

'''

salario = float(input("Qual o valor do salário? "))
if salario <=0:
    print("Somente valor acima de 0")

else:
    print("Lembrando que o valor da prestação é de 30% do salario, ou seja, R$", salario*0.30)

    prestacao = float(input("Qual o valor da prestação? "))

    limite = salario * 0.30

    if prestacao <=0:
        print("Somente valor acima de 0")

    else:
        if prestacao > limite:
            print("Emprestimo negado!")
        else:
            print("Emprestimo aprovado!")
