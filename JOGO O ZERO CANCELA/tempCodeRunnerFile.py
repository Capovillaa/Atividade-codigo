soma = 0
ultimo_numero = 0
penultimo_numero = 0
antepenultimo_numero = 0
zeros_consecutivos = 0
n = 0
cont_desconsiderados = 0
cont_considerados = 0
while n >= 0:
    numero = int(input("Digite um número (ou um número negativo para encerrar): "))
    if numero > 0:
         cont_considerados += 1
    if numero < 0:
        break
    elif numero == 0:
            cont_desconsiderados += 1
            zeros_consecutivos += 1
            if zeros_consecutivos == 1:
                soma -= ultimo_numero
                ultimo_numero = penultimo_numero
                penultimo_numero = antepenultimo_numero
            elif zeros_consecutivos == 2:
                soma -= ultimo_numero
                ultimo_numero = penultimo_numero
            elif zeros_consecutivos == 3:
                soma -= ultimo_numero
            elif  zeros_consecutivos > 3:
                cont_desconsiderados -= 1
                print(f"Só é permitido até 3 números consecutivos!!!")
    else:
        soma += numero
        antepenultimo_numero = penultimo_numero
        penultimo_numero = ultimo_numero
        ultimo_numero = numero
        zeros_consecutivos = 0
print(f"A soma dos números é {soma}")
print(f"Os numeros considerados são {cont_considerados - cont_desconsiderados}")
print(f"Os numeros desconsiderados são {cont_desconsiderados}")
