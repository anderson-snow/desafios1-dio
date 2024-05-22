import os

# Listas para armazenar os usuários e contas
usuarios = []
contas = []

# Função para cadastrar um usuário
def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado.")
            return None
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    return cpf

# Função para criar uma conta corrente
def criar_conta(cpf_usuario):
    usuario_existente = any(usuario["cpf"] == cpf_usuario for usuario in usuarios)
    
    if not usuario_existente:
        print("Usuário não encontrado.")
        return None

    numero_conta = len(contas) + 1

    contas.append({
        "agencia": "0001",
        "numero_conta": numero_conta,
        "cpf_usuario": cpf_usuario,
        "saldo": 0.0,
        "extrato": [],
        "numero_saques": 0  # Inicializa o contador de saques
    })
    return numero_conta

# Função para listar contas
def listar_contas():
    print("====== Lista de Contas =====")
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | CPF do usuário: {conta['cpf_usuario']}")
        print("------------------------")
    print("=== Fim da Lista de Contas ===")    
# Função para obter uma conta pelo número
def obter_conta_por_numero(numero_conta):
    for conta in contas:
        if conta["numero_conta"] == int(numero_conta):
            return conta
    return None

# Função de depósito
def depositar(conta, valor_deposito):
    if valor_deposito > 0:
        conta["saldo"] += valor_deposito
        conta["extrato"].append(f"Depósito de R$ {valor_deposito:.2f}")
        print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")
    return conta["saldo"], conta["extrato"]

# Função para obter o extrato
def obter_extrato(saldo, extrato):
    print("======== Extrato ========")
    print("Movimentações:")
    for movimentacao in extrato:
        print(movimentacao)
    print("-------------------------")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("====== Fim-Extrato ======")

# Função para atualizar saldo e extrato de uma conta
def atualizar_saldo_e_extrato(conta, saldo, extrato, numero_saques):
    conta["saldo"] = saldo
    conta["extrato"] = extrato
    conta["numero_saques"] = numero_saques

# Função de saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Limite diário de saques atingido.")
        return saldo, extrato, numero_saques

    if valor > limite:
        print(f"O valor máximo por saque é de R$ {limite:.2f}.")
        return saldo, extrato, numero_saques
    
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return saldo, extrato, numero_saques

    if valor > 0:
        saldo -= valor
        extrato.append(f"Saque de R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("O valor do saque deve ser positivo.")
    
    return saldo, extrato, numero_saques

# Função para mostrar o menu
def mostrar_menu():
    print("======== Banco DIO ========")
    print("|   1 - Cadastrar Usuário  |")
    print("|   2 - Criar Conta        |")
    print("|   3 - Listar Contas      |")
    print("|   4 - Depositar          |")
    print("|   5 - Sacar              |")  
    print("|   6 - Extrato            |")  
    print("|   0 - Fechar Sistema     |") 
    print("===========================")

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal
def main():
    while True:
        limpar_tela()
        mostrar_menu()
        
        opcao = input("Digite a opção desejada: ")

        limpar_tela()

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            cpf = input("Digite o CPF do usuário: ")
            endereco = input("Digite o endereço completo do usuário (logradouro, nro - bairro - cidade/UF): ")
            cpf_cadastrado = cadastrar_usuario(nome, data_nascimento, cpf, endereco)
            if cpf_cadastrado:
                print("Usuário cadastrado com sucesso.")
            else:
                print("Falha ao cadastrar usuário.")
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário: ")
            numero_conta = criar_conta(cpf)
            if numero_conta:
                print(f"Conta corrente criada com sucesso. Número da conta: {numero_conta}")
            else:
                print("Falha ao criar conta.")
        elif opcao == "3":
            listar_contas()
        elif opcao == "4":
            numero_conta = input("Digite o número da conta: ")
            valor_deposito = float(input("Digite o valor para depósito: "))
            conta = obter_conta_por_numero(numero_conta)
            if conta:
                saldo, extrato = depositar(conta, valor_deposito)
                atualizar_saldo_e_extrato(conta, saldo, extrato, conta["numero_saques"])
                print("Depósito realizado com sucesso.")
            else:
                print("Conta não encontrada.")
        elif opcao == "5":
            numero_conta = input("Digite o número da conta: ")
            valor_saque = float(input("Digite o valor para saque: "))
            conta = obter_conta_por_numero(numero_conta)
            if conta:
                saldo, extrato, numero_saques = sacar(saldo=conta["saldo"], valor=valor_saque, extrato=conta["extrato"], limite=500.00, numero_saques=conta["numero_saques"], limite_saques=3)
                atualizar_saldo_e_extrato(conta, saldo, extrato, numero_saques)
            else:
                print("Conta não encontrada.")
        elif opcao == "6":
            numero_conta = input("Digite o número da conta: ")
            conta = obter_conta_por_numero(numero_conta)
            if conta:
                obter_extrato(conta["saldo"], conta["extrato"])
            else:
                print("Conta não encontrada.")
        elif opcao == "0":
            print("Sistema finalizado, Volte Sempre!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 0 e 6.")

        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
