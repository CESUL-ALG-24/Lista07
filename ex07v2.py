soma_idade = 0

cont_homens = 0
cont_mulheres = 0

maior_idade = 0
sexo_maior_idade = ""

for i in range(3):
    while True:
        sexo = input('Informe o sexo da pessoa (M/F): ').upper()
        if sexo in ('M', 'F'):
            break

        print('Valor inválido para sexo! Informe M ou F!')

    while True:
        idade = int(input('Informe a idade da pessoa: '))
        if idade > 0:
            break

        print('Idade deve ser maior que zero!')

    soma_idade += idade

    if sexo == 'M':
        cont_homens += 1
    else:
        cont_mulheres += 1

    if idade > maior_idade:
        maior_idade = idade
        sexo_maior_idade = sexo


media_idade = soma_idade / 3

print(f"A média de idade das pessoas é {media_idade:.1f}")
print(f"Foram informados {cont_homens} homens")
print(f"Foram informados {cont_mulheres} mulheres")

print(f"A pessoa mais velha tem {maior_idade} anos e é do sexo {sexo_maior_idade}")
