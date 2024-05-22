class Transacao:
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(self)
            print(f"Depósito de R$ {self.valor:.2f} realizado com sucesso.")
            return True
        else:
            print("O valor do depósito deve ser positivo.")
            return False


class Saque(Transacao):
    def registrar(self, conta):
        if conta.limite_saques <= conta.numero_saques:
            print("Limite diário de saques atingido.")
            return False

        if self.valor > conta.limite:
            print(f"O valor máximo por saque é de R$ {conta.limite:.2f}.")
            return False

        if self.valor > conta.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return False

        if self.valor > 0:
            conta.saldo -= self.valor
            conta.numero_saques += 1
            conta.historico.adicionar_transacao(self)
            print(f"Saque de R$ {self.valor:.2f} realizado com sucesso.")
            return True
        else:
            print("O valor do saque deve ser positivo.")
            return False


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Conta:
    def __init__(self, cliente, numero):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()

    def depositar(self, valor):
        transacao = Deposito(valor)
        return transacao.registrar(self)

    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self.limite = 500.0
        self.limite_saques = 3
        self.numero_saques = 0

    def sacar(self, valor):
        transacao = Saque(valor)
        return transacao.registrar(self)


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


# Função para exibir o menu
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
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


# Função principal
def main():
    clientes = []
    contas = []

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
            cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
            clientes.append(cliente)
            print("Usuário cadastrado com sucesso.")
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário: ")
            cliente = next((c for c in clientes if c.cpf == cpf), None)
            if cliente:
                numero_conta = len(contas) + 1
                conta = ContaCorrente(cliente, numero_conta)
                cliente.adicionar_conta(conta)
                contas.append(conta)
                print(f"Conta corrente criada com sucesso. Número da conta: {numero_conta}")
            else:
                print("Usuário não encontrado.")
        elif opcao == "3":
            print("=== Lista de Contas ===")
            for conta in contas:
                print(f"Agência: {conta.agencia} | Conta: {conta.numero} | CPF do usuário: {conta.cliente.cpf}")
        elif opcao == "4":
            numero_conta = int(input("Digite o número da conta: "))
            valor_deposito = float(input("Digite o valor para depósito: "))
            conta = next((c for c in contas if c.numero == numero_conta), None)
            if conta:
                conta.depositar(valor_deposito)
            else:
                print("Conta não encontrada.")
        elif opcao == "5":
            numero_conta = int(input("Digite o número da conta: "))
            valor_saque = float(input("Digite o valor para saque: "))
            conta = next((c for c in contas if c.numero == numero_conta), None)
            if conta:
                conta.sacar(valor_saque)
            else:
                print("Conta não encontrada.")
        elif opcao == "6":
            numero_conta = int(input("Digite o número da conta: "))
            conta = next((c for c in contas if c.numero == numero_conta), None)
            if conta:
                print("======== Extrato ========")
                print("Movimentações:")
                for transacao in conta.historico.transacoes:
                    tipo = "Depósito" if isinstance(transacao, Deposito) else "Saque"
                    print(f"{tipo} de R$ {transacao.valor:.2f}")
                print("-------------------------")
                print(f"Saldo atual: R$ {conta.saldo:.2f}")
                print("====== Fim-Extrato ======")
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
