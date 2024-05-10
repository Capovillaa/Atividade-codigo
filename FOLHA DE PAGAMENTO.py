def imposto_renda (salario):
    if (salario <= 2259.20):
        imposto = 0
    elif (salario <= 2828.65):
        imposto = 0.075    
    elif (salario <= 3751.05):
        imposto = 0.15
    elif (salario <= 4664.68):
        imposto = 0.225
    elif (salario > 4664.68):
        imposto = 0.275
    return imposto

def verificacao_cod (codigo_funcao):
    verificacao_cod = 0
    while (verificacao_cod == 0):
        if(codigo_funcao != 101) and (codigo_funcao != 102):
            print("ESTE CÓDIGO DE FUNÇÃO NÃO EXISTE!!!")
            codigo_funcao = int(input("Digite um código existente: "))
        else:
            verificacao_cod=1
    return codigo_funcao

def calculo_salario_bruto101 (numero_de_faltas):
    if (codigo_funcao==101):
        volumevenda = float(input("Digite o volume de vendas deste funcionário no mês: R$ "))
        salario_bruto_semfaltas = (1500+(0.09*volumevenda))  
        desconto_faltas = numero_de_faltas * (salario_bruto_semfaltas/30)
        salario_bruto_final = salario_bruto_semfaltas - desconto_faltas
        return salario_bruto_final

def calculo_salario_bruto102 (numero_de_faltas):
    salario_bruto_semfaltas = float(input("Digite o salário bruto deste funcionário: ")) 
    while(salario_bruto_semfaltas < 2150) or (salario_bruto_semfaltas > 6950):
        print("!!!SALÁRIO BRUTO INVÁLIDO!!!")  
        salario_bruto_semfaltas = float(input("Digite um salário bruto válido: "))   
    desconto_faltas = numero_de_faltas * (salario_bruto_semfaltas/30)
    salario_bruto_final = salario_bruto_semfaltas - desconto_faltas
    return salario_bruto_final

def calculo_salario_liquido (salario_bruto,imposto):
    salario_liquido = salario_bruto - (salario_bruto * imposto ) 
    return salario_liquido

print("\n     BEM VINDO AO SOFTWARE FOLHA DE PAGAMENTO")
print('-'*50)

dict_funcionarios = {}
inf_funcionarios=[]
loop = 0

while(loop==0):

    menu=int(input("1: Inserir Funcionários\n2: Remover Funcionários\n3: Folha Pagamento\n\nSelecione: "))
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

            if (codigo_funcao == 101):
                salario_bruto101 = calculo_salario_bruto101(num_faltas)
                imposto101 = imposto_renda(salario_bruto101)
                salario_liquido = calculo_salario_liquido(salario_bruto101,imposto101)
            elif(codigo_funcao == 102):
                salario_bruto102 = calculo_salario_bruto102(num_faltas)
                imposto102 = imposto_renda(salario_bruto102)
                salario_liquido = calculo_salario_liquido(salario_bruto102,imposto102) 

            inf_funcionarios.append(nome_funcionario.title())
            inf_funcionarios.append(codigo_funcao)
            inf_funcionarios.append(num_faltas)
            inf_funcionarios.append(salario_liquido)
            dict_funcionarios[matricula] = inf_funcionarios
            inf_funcionarios=[]

            print('-'*50)

    print(dict_funcionarios)

    if(menu==2):

        remover_funcionário=int(input("Digite a mátricula do funcionário que será removido: "))

        if remover_funcionário in dict_funcionarios:
            dict_funcionarios.pop(remover_funcionário)
            print('-'*50)
            print("Funcionário removido com sucesso!")
            print('-'*50)
        else:
            print('-'*50)
            print("Funcionário não encontrado.")
            print('-'*50)
    
    if menu == 3:
        folha_pagamento=int(input("Digite o número da matricula do funcionario que deseja determinar a folha de pagamento: "))
        if folha_pagamento in dict_funcionarios:
            print('-'*50)
            print(f"Matricula: {folha_pagamento}\nValores: {dict_funcionarios[folha_pagamento]}")
            print('-'*50)
        else:
            print('-'*50)
            print("Esse número de matricula não existe")
            print('-'*50)
