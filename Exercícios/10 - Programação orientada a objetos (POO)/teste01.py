class Calculos:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        print(f"O resultado da soma entre {self.a} e {self.b} é igual a: {self.a + self.b}")
    
    def subtrair(self):
        print(f"O resultado da subtração entre {self.a} e {self.b} é igual a: {self.a - self.b}")
    
    def multiplicar(self):
        print(f"O resultado da multiplicação entre {self.a} e {self.b} é igual a: {self.a * self.b}")
    
    def dividir(self):
        print(f"O resultado da divisão entre {self.a} e {self.b} é igual a: {self.a / self.b}")
    
    def resto(self):
        print(f"O resto da divisão entre {self.a} e {self.b} é igual a: {self.a % self.b}")
    
somando = Calculos(15, 7)
somando.somar()

subtraindo = Calculos(15, 7)
subtraindo.subtrair()

multiplicando = Calculos(15, 7)
multiplicando.multiplicar()

dividindo = Calculos(15, 7)
dividindo.dividir()

resto = Calculos(15, 7)
resto.resto()


