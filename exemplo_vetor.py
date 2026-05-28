#exemplo 1 : VETOR 
n = int(input('Digite o tamanho do vetor:'))
vetor = []

i=1
while i <= n:
    valor = int(input(f'digite o valor da posição{i}:1'))
    vetor.append (valor)
    i+=1
print (vetor)