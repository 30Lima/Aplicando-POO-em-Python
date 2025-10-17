#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def mostrar_carro():
        for carro in Carro.carros:
            print (f'{carro.modelo} | {carro.cor} | {carro.ano}')
    
civic = Carro('Honda Civic', 'Azul', '1998')
Carro.mostrar_carro()

    