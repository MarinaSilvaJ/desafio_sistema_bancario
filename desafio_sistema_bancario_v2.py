saldo = 0
limite = 500
extrato = ""
usuarios = []
contas = []
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

def menu(): 
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta Corrente
    [lc] Listar Contas 
    [q] Sair

    => """
    return input(menu)

def depositar(saldo, extrato, /):
    print("Depósito")

    deposito = float(input("Informe o valor que deseja depositar: "))

    if deposito > 0:
        saldo += deposito
        extrato += f"- Depósito: R${deposito:.2f} \n"
        print(f"Depósito de {deposito:.2f} reais efetuado com sucesso! Verifique seu extrato.")
    else:
        print("Não é possível depositar valor zero ou negativo, por gentileza refaça a operação.") 
    return saldo, extrato 
 
def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
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
    return saldo, extrato, numero_saques
        
def imp_extrato(saldo, /, *, extrato):
    print("*Extrato*".center(50,"."))
    print(extrato if extrato else "Não foi realizada nenhuma movimentação nessa operação. \n")
    print(f"Saldo Total: R${saldo:.2f}".center(50,"."))

def novo_usuario(usuarios):
    confirma = "N"
    cpf = input("Por favor, informe o seu CPF: ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já existente no sistema!")
            return
        
    while confirma == "N" or confirma == "n":
        nome = input("Informe seu nome completo: ")
        data_nascimento = input("Informe sua data de nascimento (formato dd/mm/aaa): ")
        endereco = input("Informe seu endereço (Logradouro, nro - Bairro - Cidade/Sigla Estado): ")
        confirma = input(f"Confirma as informações abaixo? Digite 'S' ou 'N' \n Nome: {nome}, CPF: {cpf}, Data de Nascimento: {data_nascimento}, Endereço: {endereco} \n")

        if confirma == "S" or confirma == "s":
            usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
            print(f"Bem Vindo(a) {nome}, seu usuário foi cadastrado com sucesso!")
        elif confirma == "N" or confirma == "n":
            print("Por gentileza, entre novamente com seus dados.")
        else:
            print("Opção inválida, usuário não cadastrado.")
            return


def nova_conta(agencia, usuarios, num_conta):
    cpf = input("Por favor, informe o seu CPF: ") 

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            break   
    else:
        print("Usuário sem cadastro no sistema, por favor criar uma conta de usuário antes de criar a conta corrente.")
        return

    contas.append({"agencia": agencia, "cc": num_conta, "usuario": usuario["cpf"]})
    print(f"Conta criada com sucesso! \n Agência: {agencia} - Conta Corrente: {num_conta} - Cliente: {usuario["nome"]} - {usuario["cpf"]}")

def lista_contas(contas):
    lista = "*Lista de Contas*".center(50,".")

    for conta in contas:
        lista += f"\n Agência: {conta["agencia"]} - CC: {conta["cc"]} - CPF Cliente: {conta["usuario"]} \n"

    lista += "".center(50,".")     
    print(lista)

while True:
    opcao = menu()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
                          
    elif opcao == "e":
        imp_extrato(saldo,extrato=extrato)
    
    elif opcao == "nu":
        novo_usuario(usuarios)
    
    elif opcao == "nc":
        num_conta = len(contas) + 1
        nova_conta(AGENCIA, usuarios, num_conta)
    
    elif opcao == "lc":
        lista_contas(contas)
    
    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecionar a opção que corresponde a operação desejada informada na lista.")