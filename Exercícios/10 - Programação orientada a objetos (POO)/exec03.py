# Conceito de Encapsulamento
"Encapsulamento: Encapsulamento é a prática de esconder os detalhes internos de uma classe e expor apenas o necessário. Isso protege os dados e garante que o acesso e a modificação sejam controlados.  Atributos Privados: Usamos atributos privados (com prefixo __) para evitar acesso direto de fora da classe. Métodos Públicos: Prover métodos públicos para permitir a manipulação desses dados de forma controlada."

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  #  O uso de __ no início do nome do atributo indica que ele é privado, e só deve ser acessado dentro da classe.

    def depositar(self, quantia):
        if quantia > 0:
            self.__saldo += quantia

    def sacar(self, quantia):
        # Verifique se a quantia é maior que 0 e, ao mesmo tempo, menor ou igual ao saldo, para não permitir sacar dinheiro que não existe.
        if 0 < quantia <= self.__saldo:
            self.__saldo -= quantia

    def exibir_saldo(self):
        return self.__saldo

# Usando a classe ContaBancaria
conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(30)
print(conta.exibir_saldo())  # Saída: 120
