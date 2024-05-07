def calculo_salario_bruto101 ():
    if (codigo_funcao==101):
        volumevenda=float(input("Digite o volume de vendas deste funcionário do mês: "))
        salario_bruto101 = (1500+(0.09*volumevenda))
        return salario_bruto101

def verificacao_salario102(salario): 
    while(salario < 2150) or (salario > 6950):
        print("!!!SALÁRIO BRUTO INVÁLIDO!!!")  
        salario=float(input("Digite o salário bruto deste funcionário: "))  
    return salario

dict_funcionarios = {}
inf_funcionarios=[]
qnt_funcionarios = int(input("Digite a Quantidade de funcionários que deseja cadastrar: "))
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

print(dict_funcionarios)
print('-'*50)
menu=int(input("1: Busca Livro pelo Título\n2: Busca livro pelo Código\n3: Dados Livros preço superior a 50\nSelecione:"))
if(menu==1):
    cont=0
    busca_livro_nome=input("Digite o título do livro que deseja as informaçoes: ")
    for matricula, inf_funcionarios in livros.items():
        if (inf_funcionarios[0] == busca_livro_nome.title()):
            print(f"As informações são:\nCódigo: {matricula}\nNome: {inf_funcionarios[0]}\nAutor: {inf_funcionarios[1]}\nPreço: {inf_funcionarios[2]}")
            cont+=1
    if cont == 0:
        print("Não Existe")
if(menu==2):
    busca_livro_cod = int(input("Digite o código do livro que deseja as informções: "))
    if busca_livro_cod in livros:
        print(f"As informações são:\n{livros[busca_livro_cod]}")
    else:
        print('Não existe')
if(menu==3):
    livros50=0
    for matricula, inf_funcionarios in livros.items():
        if (inf_funcionarios[2]> 50):
            print(f"As informações são:\nCódigo: {matricula}\nNome: {inf_funcionarios[0]}\nAutor: {inf_funcionarios[1]}\nPreço: {inf_funcionarios[2]}")
            livros50+=1
    if(livros50==0):
        print("Não possui nenhum livro com valor maior que R$50")