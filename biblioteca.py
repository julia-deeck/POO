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