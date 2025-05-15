class Pessoa():
    def __init__(self,nome,idade,peso):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=False
        self.dormindo=False
        self.falando=False

    def apresentar(self):
        print(f"Olá meu nome é {self.nome}. "
              f"Eu tenho {self.idade} anos e peso {self.peso} quilos")

    def Comer(self):
        if self.dormindo == True:
            print("Você está dormindo, você não pode comer!")
        elif self.falando == True:
            print("Você está falando, você não pode comer!")
        else:
            self.comendo = True
            print(f"{self.nome} está comendo")

    def Dormir(self):
        if self.comendo == True:
            print("Você está comendo, você não pode dormir!")
        elif self.falando == True:
            print("Você está falando, você não pode dormir!")
        else:
            self.dormindo = True
            print(f"{self.nome} está dormindo")

    def Falar(self):
        if self.comendo == True:
            print("Você está comendo, você não pode falar!")
        elif self.dormindo == True:
            print("Você está dormindo, você não pode falar!")
        else:
            self.falando = True
            print(f"{self.nome} está falando")

#------------------------------------------------------------------------------------------------------------
class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"O {self.nome} está miando...")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"O {self.nome} está latindo...")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def chiar(self):
        print(f"O {self.nome} está chiando")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def mugir(self):
        print(f"O {self.nome} está mugindo...")

#------------------------------------------------------------------------------------------------------------
class Ingresso():
    def __init__(self,valor):
        self.valor=valor
    def imprimeValor(self):
        print(f"Valor do ingresso: R${self.valor}")

class VIP(Ingresso):
    def __init__(self,valor):
        super().__init__(valor*1.5)
    def imprimeValor(self):
        print(f"Valor do ingresso VIP: R${self.valor}")

#------------------------------------------------------------------------------------------------------------
class Forma():
    def __init__(self):
        self.area= 0
        self.perimetro= 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self,base,altura):
        self.area = base*altura
        print(f"Área do retângulo: {self.area}")

    def calcularPerimetro(self,base,altura):
        self.perimetro = 2*(base+altura)
        print(f"Perímetro do retângulo: {self.perimetro}")

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self,base,altura):
        self.area = (base*altura)/2
        print(f"Área do triângulo: {self.area}")

    def calcularPerimetro(self,lado):
        self.perimetro = lado*3
        print(f"Perímetro do triângulo: {self.perimetro}")