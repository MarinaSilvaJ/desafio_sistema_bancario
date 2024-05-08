menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")

        deposito = float(input("Informe o valor que deseja depositar: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"- Depósito: R${deposito:.2f} \n"
            print(f"Depósito de {deposito:.2f} reais efetuado com sucesso! Verifique seu extrato.")
        else:
            print("Não é possível depositar valor zero ou negativo, por gentileza refaça a operação.")
    
    elif opcao == "s":
        print("Saque")

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saque diário atingido! Por favor tente novamente amanhã.")
        else:
            saque = float(input("Informe o valor que deseja sacar: "))

            if saque > limite:
                print(f"Limite maximo de R${limite:.2f} reais atingido, por favor refaça a operação com valor inferior ao seu limite.")
            elif saque > saldo:
                print(f"Saldo insuficiente para este saque, seu saldo é R${saldo:.2f} reais.")
            elif saque <= 0:
                print("Não é possível efetuar um saque de valor zero ou negativo, refaça a operação.")
            else:
                saldo -= saque
                numero_saques += 1
                extrato += f"- Saque: R${saque:.2f} \n"
                print(f"Saque de R${saque:.2f} reais efetuado com sucesso! Verifique seu extrato para saber o valor da sua conta.")
                          
    elif opcao == "e":
        print("*Extrato*".center(50,"."))
        print(extrato if extrato else "Não foi realizada nenhuma movimentação nessa operação. \n")
        print(f"Saldo Total: R${saldo:.2f}".center(50,"."))
    
    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecionar a opção que corresponde a operação desejada informada na lista.")