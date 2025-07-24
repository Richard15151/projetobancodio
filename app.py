import textwrap
import os


def menu():
    menu = """\n
    -------------- MENU --------------
        Bem vindo! selecione a opção que deseja:

        [1]\tdepositar
        [2]\tsacar
        [3]\textrato
        [4]\tcriar usuário
        [5]\tcriar conta corrente
        [6]\tlistar contas
        [0]\tsair
        => """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("=== Depósito realizado com sucesso! ===")
        os.system("pause")
        os.system("cls")
    else:
        print("@@@ valor de depósito inválido!. @@@")
        os.system("pause")
        os.system("cls")
    return saldo, extrato

def saque (*, saldo, valor_saque, extrato, limite, LIMITE_SAQUES, numero_saques):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saque = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("@@@ Valor de saque é maior que o saldo! Operação recusada. @@@")
        os.system("pause")
        os.system("cls")
    elif excedeu_limite:
        print("@@@ Valor de saque excedeu o limite máximo por saque! Operação recusada @@@")
        os.system("pause")
        os.system("cls")
    elif excedeu_saque:
        print("@@@ Limite diário de saques excedido! Tente novamente amanhã. @@@")
        os.system("pause")
        os.system("cls")
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"\nSaque: \t\tR$ {valor_saque:.2f}\n"
        numero_saques +=1
        print("=== Saque realizado com sucesso! ===")
        os.system("pause")
        os.system("cls")
    else:
        print("@@@ Valor de saque inválido! @@@")
        os.system("pause")
        os.system("cls")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n ============== EXTRATO ===============")
    print("Não foram realizadas transações" if not extrato else extrato)
    print(f"\nSaldo: \t\tR${saldo:.2f}")
    print("========================================")
    os.system("pause")
    os.system("cls")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        os.system("pause")
        os.system("cls")
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigladoestado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")
    os.system("pause")
    os.system("cls")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    os.system("pause")
    os.system("cls")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        os.system("pause")
        os.system("cls")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(
                saldo=saldo,
                valor_saque=valor,
                extrato=extrato,
                limite=limite,
                LIMITE_SAQUES=LIMITE_SAQUES,
                numero_saques=numero_saques
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Saindo")
            os.system("cls")
            break

        else:
            print("Opção inválida! selecione outra opção")
            os.system("pause")
            os.system("cls")

main()