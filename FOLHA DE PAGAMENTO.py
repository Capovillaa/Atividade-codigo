def calculo_salario_bruto101 ():
    if (codigo_funcao==101):
        volumevenda=float(input("Digite o volume de vendas deste funcionário do mês: R$ "))
        salario_bruto101 = (1500+(0.09*volumevenda))
        return salario_bruto101

def verificacao_salario102(salario): 
    while(salario < 2150) or (salario > 6950):
        print("!!!SALÁRIO BRUTO INVÁLIDO!!!")  
        salario=float(input("Digite o salário bruto deste funcionário: "))  
    return salario

loop=0

print('-'*50)

dict_funcionarios = {}
inf_funcionarios=[]
while(loop==0):

    menu=int(input("1: Inserir Funcionários\n2: Remover Funcionários\n\nSelecione: "))
    print('-'*50)
    if(menu==1):
        qnt_funcionarios = int(input("Digite a Quantidade de funcionários que deseja cadastrar: "))
        print('-'*50)
        for i in range(qnt_funcionarios):
            matricula = int(input(f"Qual a mátricula do {i+1}°funcionário: "))
            nome_funcionario = (input(f"Qual o nome do {i+1}°funcionário: "))
            codigo_funcao = int(input("Digite o código da função deste funcionário: "))
            num_faltas = int(input(f"Digite o número de faltas deste funcionário: "))
            if (codigo_funcao==101):
                salario_bruto=calculo_salario_bruto101()
            elif(codigo_funcao==102):
                salario102=float(input("Digite o salário bruto deste funcionário: "))
                salario_bruto=verificacao_salario102(salario102)
            inf_funcionarios.append(nome_funcionario.title())
            inf_funcionarios.append(codigo_funcao)
            inf_funcionarios.append(num_faltas)
            inf_funcionarios.append(salario_bruto)
            dict_funcionarios[matricula] = inf_funcionarios
            inf_funcionarios=[]
            print('-'*50)

    if(menu==2):
        remover_funcionário=int(input("Digite a mátricula do funcionário que será removido: "))
        if remover_funcionário in dict_funcionarios:
            dict_funcionarios.pop(remover_funcionário)
            print('-'*50)
            print("Funcionário removido com sucesso!")
            print('-'*50)
        else:
            print('-'*50)
            print("Funcionário não encontrado.\n")
            print('-'*50)
