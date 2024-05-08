num = int(input("Informe um número inteiro: "))

for i in range(num + 1):
    if (i % 3 == 0) or (i % 7 == 0):
        print("*")
    else:
        print(i)
