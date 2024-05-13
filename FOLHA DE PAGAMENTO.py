def verificacao_cod (codigo_funcao):
    verificacao_cod = 0
    while (verificacao_cod == 0):
        if(codigo_funcao != 101) and (codigo_funcao != 102):
            print("ESTE CÓDIGO DE FUNÇÃO NÃO EXISTE!!!")
            codigo_funcao = int(input("Digite um código existente: "))
        else:
            verificacao_cod=1
    return codigo_funcao

def calculo_salario_bruto (codigo_funcao,num_faltas):

    if (codigo_funcao == 101):
        volumevenda = float(input("Digite o volume de vendas deste funcionário no mês: R$ "))
        salario_bruto = (1500+(0.09*volumevenda))
        desconto_faltas = num_faltas * (salario_bruto/30)
        salario_bruto = salario_bruto - desconto_faltas

    elif(codigo_funcao == 102):
        salario_bruto = float(input("Digite o salário bruto deste funcionário: R$ ")) 
        while(salario_bruto < 2150) or (salario_bruto > 6950):
            print("!!!SALÁRIO BRUTO INVÁLIDO!!!")  
            salario_bruto = float(input("Digite um salário bruto válido: R$ "))   
        desconto_faltas = num_faltas * (salario_bruto/30)
        salario_bruto = salario_bruto - desconto_faltas
    return salario_bruto

def calculo_salario_liquido_e_imposto (salario_bruto):
    if (salario_bruto <= 2259.20):
        imposto = 0
    elif (salario_bruto <= 2828.65):
        imposto = 0.075    
    elif (salario_bruto <= 3751.05):
        imposto = 0.15
    elif (salario_bruto <= 4664.68):
        imposto = 0.225
    elif (salario_bruto > 4664.68):
        imposto = 0.275
    salario_liquido = salario_bruto - (salario_bruto * imposto ) 
    return salario_liquido, imposto

def imprimir_folha_pagamento (matricula, inf):
    nome_funcionario = inf[0]
    codigo_funcao = inf[1]
    num_faltas = inf[2]
    salario_liquido = inf[4]

    print('-' * 50)
    print(f"Matrícula: {matricula}")
    print(f"Nome do funcionário: {nome_funcionario}")
    print(f"Código da função: {codigo_funcao}")
    print(f"Número de faltas: {num_faltas}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")
    print('-' * 50)




print("\n     BEM VINDO AO SOFTWARE FOLHA DE PAGAMENTO")
print('-'*50)

dict_funcionarios = {}
inf_funcionarios=[]
lista_salarios_brutos=[]
loop = 0

while(loop==0):

    menu=int(input("1: Inserir Funcionários\n2: Remover Funcionários\n3: Folha Pagamento\n4: Relatório de todos os funcionários\n\nSelecione: "))
    print('-'*50)

    if(menu==1):

        qnt_funcionarios = int(input("Digite a Quantidade de funcionários que deseja cadastrar: "))

        print('-'*50)

        for i in range(qnt_funcionarios):
            matricula = int(input(f"Qual a mátricula do {i+1}°funcionário: "))
            nome_funcionario = (input(f"Qual o nome do {i+1}°funcionário: "))
            codigo_funcao = int(input("Digite o código da função deste funcionário: "))
            codigo_funcao = verificacao_cod(codigo_funcao) 
            num_faltas = int(input(f"Digite o número de faltas deste funcionário: "))
            salario_bruto = calculo_salario_bruto(codigo_funcao,num_faltas)
            salario_liquido,imposto = calculo_salario_liquido_e_imposto(salario_bruto)

            inf_funcionarios.append(nome_funcionario.title())
            inf_funcionarios.append(codigo_funcao)
            inf_funcionarios.append(num_faltas)
            inf_funcionarios.append(salario_bruto)
            inf_funcionarios.append(salario_liquido)
            inf_funcionarios.append(imposto)
            dict_funcionarios[matricula] = inf_funcionarios
            inf_funcionarios=[]

            lista_salarios_brutos.append(salario_bruto)

            print('-'*50)
    print(dict_funcionarios)
    if(menu == 2):

        remover_funcionário = int(input("Digite a mátricula do funcionário que será removido: "))

        if remover_funcionário in dict_funcionarios:
            dict_funcionarios.pop(remover_funcionário)
            print('-'*50)
            print("Funcionário removido com sucesso!")
            print('-'*50)
        else:
            print('-'*50)
            print("Funcionário não encontrado.")
            print('-'*50)
    
    if (menu == 3):

        folha_pagamento = int(input("Digite o número da matrícula do funcionário que deseja visualizar a folha de pagamento: "))

        if folha_pagamento in dict_funcionarios:
            imprimir_folha_pagamento(folha_pagamento, dict_funcionarios[folha_pagamento])
        else:
            print('-' * 50)
            print("Essa matrícula não corresponde a nenhum funcionário.")
            print('-' * 50)

    if (menu == 4):
        
        for k in dict_funcionarios.items():
            matricula = k[0]
            nome_funcionario = k[1][0]
            codigo_funcao = k[1][1]
            salario_bruto = k[1][3]
            salario_liquido = k[1][4]

            print('-' * 50)
            print(f"\nMatrícula: {matricula}")
            print(f"Nome do funcionário: {nome_funcionario}")
            print(f"Código da função: {codigo_funcao}")
            print(f"Salário bruto: R$ {salario_bruto:.2f}")
            print(f"Salário líquido: R$ {salario_liquido:.2f}\n")

        print('-' * 50)
