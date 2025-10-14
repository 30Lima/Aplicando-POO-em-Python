class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)


    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()

#print(restaurante_praca) -> exibição da alocação na memória
#print(dir(restaurante_praca)) -> todas informações do objeto
#print(vars(restaurante_praca)) -> exibição do conteúdo da classe em um dicionário

#print(restaurante_praca.ativo) -> exibição de um objeto expecífico
