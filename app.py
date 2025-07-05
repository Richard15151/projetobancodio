import os

menu = '''
Bem vindo! selecione a opção que deseja:

[1] depositar
[2] sacar
[3] extrato
[0] sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = input("Sua opção:")

    if opcao == "1":
        print("Depósito")
        valor_deposito = float(input("Informe o valor do depósito:"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
            os.system("pause")
            os.system("cls")
        else:
            print("valor de depósito inválido!")
            os.system("pause")
            os.system("cls")

    elif opcao == "2":
        print("Sacar")
        valor_saque = int(input("Informe o valor do saque:"))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Valor de saque é maior que o saldo! Operação recusada.")
            os.system("pause")
            os.system("cls")
        elif excedeu_limite:
            print("Valor de saque excedeu o limite máximo por saque! Operação recusada")
            os.system("pause")
            os.system("cls")
        elif excedeu_saque:
            print("Limite diário de saques excedido! Tente novamente amanhã.")
            os.system("pause")
            os.system("cls")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"\nSaque: R$ {valor_saque:.2f}"
            numero_saques +=1
            print("Saque realizado com sucesso!")
            os.system("pause")
            os.system("cls")
        else:
            print("Valor de saque inválido!")
            os.system("pause")
            os.system("cls")

    elif opcao == "3":
        print("EXTRATO".center(20,"#"))
        print("Não foram realizadas transações" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("#"*20)
        os.system("pause")
        os.system("cls")

    elif opcao == "0":
        print("Saindo")
        os.system("cls")
        break

    else:
        print("Opção inválida! selecione outra opção")
        os.system("pause")
        os.system("cls")