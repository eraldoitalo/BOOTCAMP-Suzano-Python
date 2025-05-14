#Criando um sistema bancario com python

# Opcoes de menu
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """

# Variaveis 
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    #configurando as funcoes da opcao 1
    if opcao == "1":
        print("Depositar")
        valor = float(input("Informe o valor a ser depositado R$: ")) # pede para o usurio informar um valor, esse valor será armazenando na variavel
        if valor > 0: 
            saldo += valor
            extrato += f"deposito: R$ {valor:.2F}\n" # o valor depositado é adicionado ao saldo e o extrato é atualizado com o valor depositado
            print(f"Deposito de R$ {valor:.2f} realizado com sucesso!") 
        else:
            print("Valor invalido!") # se o valor for menor q 0, sera informado que o valor e invalido
    # configurando as funcoes da opacao 2
    elif opcao == "2":
        print ("Sacar")
        valor = float(input("Informe o valor a ser sacado R$: ")) # pede para informar o valor que sera sacado
        excedeu_saldo = valor > saldo # varifica se o valor do saque e maior que o saldo
        excedeu_limite = valor > limite # verifica se o valor do saque e maior que o limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES # verifica se o numero de saques e maior que o limite de saques 
        if excedeu_saldo:
            print ("Voce nao possui saldo suficiente!")
        elif excedeu_limite:
            print ("Voce excedeu o limite diario!")
        elif excedeu_saques:
            print ("Voce atingiu o limite de saque diario!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print (f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print ("Valor invalido!")
    # configuando as funcoes da opcao 3
    elif opcao == "3":
        print("Extrato")
        print("Nao foram realizados movimentacoes." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
    # configurando as funcoes da opcao 0
    elif opcao == "0":
        print("Sistema encerrado!")
        break
    # configurando as funcoes da opcao invalida
    else:
        print("Opcao invalida!")

        
  
        

