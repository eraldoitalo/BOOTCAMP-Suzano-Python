import textwrap
import datetime
from datetime import datetime

def log_transacao(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__}")
        return resultado
    return wrapper

def menu():
    menu = """\n
    [1] \tDepositar
    [2] \tSacar
    [3] \tExtrato
    [4] \tNova conta
    [5] \tListar contas
    [6] \tNovo usuario
    [0] \tSair
    => """
    return input(textwrap.dedent(menu))

@log_transacao
def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2F}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido!")
    return saldo, extrato
@log_transacao
def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Voce nao possui saldo suficiente!")
    elif excedeu_limite:
        print("Voce excedeu o limite diario!")
    elif excedeu_saques:
        print("Voce atingiu o limite de saque diario!")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}/n"
        numero_saques += 1
        print(f"Saques de R$ {valor:.2f} realizado com sucesso!")
    
    else:
        print("Valor invalido!")
    return saldo, extrato, numero_saques
@log_transacao
def exibir_extrato(saldo, /, *, extrato):
    print("Extrato")
    print("Nao foram realizadas movimentacoes." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
@log_transacao
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuario ja possui cadastro!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco: ")

    usuarios.append({"nome": nome, "data_nacimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario cadastrado com sucesso!")
@log_transacao  
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None    
@log_transacao
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario nao encontrado.")
@log_transacao
def listar_contas(contas):
    for conta in contas:
        linha = f"""Agencia: {conta ["agencia"]}
        conta: {conta ["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
        """
        print("-" * 100)
        print(textwrap.dedent(linha))

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
            valor = float(input("Informe o valor a ser depositado R$: ")) 

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor a ser sacado R$: ")) 
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "6":
            criar_usuario(usuarios)
        
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == "5":
            listar_contas(contas)
        
        elif opcao == "0": 
            break
        
        else:
            print("Opcao invalida!")

main()
