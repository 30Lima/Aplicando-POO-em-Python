class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

print(vars(restaurante_praca))
print(vars(restaurante_pizza))

#print(restaurante_praca) -> exibição da alocação na memória
#print(dir(restaurante_praca)) -> todas informações do objeto
#print(vars(restaurante_praca)) -> exibição do conteúdo da classe em um dicionário

#print(restaurante_praca.ativo) -> exibição de um objeto expecífico
