n=0
cont_0=0
soma=0
while(n >= 0):
    n=int(input("Numero:"))
    if (n < 0):
        break
    elif(n == 0):
        cont_0 += 1
        if(cont_0 > 3):
            print(f"Só é permitido até 3 números consecutivos!!!")
            if(cont_0>=3):
                cont_0=0
                n=int(input("Numero:"))
                if(n==0):
                    print(f"Só é permitido até 3 números consecutivos!!!")           
    soma +=n
print(f"Soma total={soma}")