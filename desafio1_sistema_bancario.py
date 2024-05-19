import os

def depositar(saldo, depositos):
    print("======== Depósito ========")
    valor = float(input("Digite o valor para depósito: "))
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        print("-------------------------")
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo

def sacar(saldo, saques, total_saques, limite_saques):
    print("======== Saque ========")
    if total_saques >= limite_saques:
        print("Limite diário de saques atingido.")
        return saldo, total_saques

    valor = float(input("Digite o valor para saque: "))
    if valor > 500:
        print("O valor máximo por saque é de R$ 500.00.")
        return saldo, total_saques
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return saldo, total_saques
    if valor > 0:
        saldo -= valor
        saques.append(valor)
        total_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        print("-------------------------")
    else:
        print("O valor do saque deve ser positivo.")
    
    return saldo, total_saques

def extrato(depositos, saques, saldo):
    print("======== Extrato ========")
    print("Depósitos:")
    for deposito in depositos:
        print(f"R$ {deposito:.2f}")
    print("-------------------------")    
    print("Saques:")
    for saque in saques:
        print(f"R$ {saque:.2f}")
    print("-------------------------")        
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("====== Fim-Extrato ======")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("======== Banco DIO ========")
    print("|   1 - Depósito          |")
    print("|   2 - Saque             |")
    print("|   3 - Extrato           |")
    print("|   4 - Sair              |")
    print("===========================")

def main():
    saldo = 0.0
    depositos = []
    saques = []
    total_saques = 0
    limite_saques = 3

    while True:
        limpar_tela()
        mostrar_menu()
        
        opcao = input("Digite a opção desejada: ")

        limpar_tela()

        if opcao == "1":
            saldo = depositar(saldo, depositos)
        elif opcao == "2":
            saldo, total_saques = sacar(saldo, saques, total_saques, limite_saques)
        elif opcao == "3":
            extrato(depositos, saques, saldo)
        elif opcao == "4":
            print("Sistema finalizado, Volte Sempre!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
