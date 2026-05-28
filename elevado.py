na = int(input("Digite o número de andares:"))
ps=0
pt=0
for c in range (1, na +1):
    print(f"andar={c}")
    pe = int(input("digite o número de pessoas que entraram do elevador neste andar:"))
   
    if c > 1:
        ps = int(input("digite o número de pessoas que sairam:"))
       
    pt = (pt + pe) - ps
    print(f"ficaram:{pt}")


    if pt > 15:
        s = pt-15
        print(f"excesso de passageiros,  precisam sair:{s}")
        pt = 15
       


   


print(f"pessoas restantes no elevador {pt}")
