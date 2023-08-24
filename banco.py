# REALIZAR DEPOSITO
#CONSTAR VALOR DE DEPOISTO
#SOMAR DEPOSITO
#REALIZAR SAQUE
#CASO SEM SALDO EXIBIR MENSAGEN SEM SALDO
#REALIZAR 3 SAQUES MAX 500,00
#ARMAZENAR SAQUES
#EXIBIR TOTAL DAS TRANSACOES
#EXIBIR OPERACAO SEJA SAQUE OU DEPOSITO
class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.movimentacoes = []
        self.saques_restantes = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.movimentacoes.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_restantes > 0 and 0 < valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            self.movimentacoes.append(f"Saque: -R${valor:.2f}")
            self.saques_restantes -= 1
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
            print(f"Saques restantes: {self.saques_restantes}")
        elif self.saques_restantes <= 0:
            print("Limite máximo de saques atingido.")
        elif valor > 500:
            print("Limite máximo de saque por transação é de R$500.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def extrato(self):
        print("Extrato:")
        for movimento in self.movimentacoes:
            print(movimento)
        print(f"Saldo final: R${self.saldo:.2f}")


def main():
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    conta = ContaBancaria(saldo_inicial)

    while True:
        print("\nOpções:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Consultar Saldo")
        print("4 - Extrato")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a depositar: "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a sacar: "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.consultar_saldo()
        elif opcao == '4':
            conta.extrato()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()

