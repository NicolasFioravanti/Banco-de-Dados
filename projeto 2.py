import time
lista = []

while True:
    nome = input('Nome: ').title()
    idade = input('Idade: ')
    cidade = input('Cidade: ').title()

    lista.append([nome, idade, cidade])

    while True:
        cont = input('Deseja continuar? S/N ').strip().upper()
        if cont == 'N' or cont == 'S':
            break
        else:
            print('Digite apenas "S" para continuar ou "N" para sair.')

    if cont == 'N':
        break

for info in lista:
    print(f'----------\n'
          f'Nome: {info[0]}\nIdade: {info[1]}\nCidade: {info[2]}')

time.sleep(10)
