num = int(input("Informe um número inteiro: "))

metade_num = int(num ** 0.5)
primo = True

for i in range(2, metade_num + 1):
    if num % i == 0:
        primo = False
        break

if primo:
    print('O número é primo!')
else:
    print('O número não é primo!')
