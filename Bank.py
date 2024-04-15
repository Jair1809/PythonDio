import textwrap

def menu():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Novo Usuario
    [6] Listar Contas
    [7] Sair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo+= valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é invalido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo= valor> saldo
    execedeu_limite = valor > limite
    execedeu_saques= numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente")
        
    elif execedeu_limite:
        print("Operação falhou! O valor do saque execede o limite.")
        
    elif execedeu_saques:
        print("Operação falhou! Numero maximo de saques excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("====Saque realizado com sucesso!====")
    
    else:
        print("Operação falhou! o valor informado é invalido.")
    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
    
def criar_usuarios(usuarios):
    cpf = input("Informe o CPF  (Somente Numeros): ")
    usuario= filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Iforme o nome completo")
    data_nascimento= input("informe a data de nascimento")
    endereco= input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome":nome, "Data de nascimento":data_nascimento, "endereco":endereco})
    
    print("Usuario criado com sucesso")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf= input("Informe o cpf do usuário")
    usuario= filtrar_usuario(cpf, usuarios)
    
    if usuario :
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 2000
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 4

    while True:

        opcao = input(menu)

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "3":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "4":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
