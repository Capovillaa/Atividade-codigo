n=0
cont_0=0
soma=0
while(n >= 0):
    n=int(input("Numero:"))
    if(n!=0):
        cont_0=0
    if (n < 0):
        break
    elif(n == 0):
        cont_0 += 1
        if(cont_0 > 3):
            print(f"Só é permitido até 3 números consecutivos!!!")
            n=int(input("Numero:"))
            if(n==0):
                print(f"Só é permitido até 3 números consecutivos!!!") 
            else:
                cont_0=0       
    soma +=n
print(f"Soma total={soma}")