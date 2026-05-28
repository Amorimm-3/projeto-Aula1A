#exemplo2 :  media
n = int(input('total de alunos:'))
vnotas = []
soma = 0

for i in range (n):
    nota = float(input(f'Digite a nota do aluno{i+1}:'))
    vnotas.append(nota)
    soma = soma = vnotas [i]

media = soma/n
acima= 0
abaixo=0

for i in range (n):
    if vnotas [i]>= media:
        acima+=1

    else:
        abaixo+=1

print(f'nota dos alunos;{vnotas}')
print(f'media da turma:{media}')
print(f'notas acima ou igual a media:{acima}')
print(f'notas abaixo da media:{abaixo}')