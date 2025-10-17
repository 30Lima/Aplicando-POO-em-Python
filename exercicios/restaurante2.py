# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão.
# Crie uma instância utilizando o construtor.

class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria, avaliacao, rodizio):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.avaliacao = avaliacao
        self.rodizio = rodizio
        Restaurante.restaurantes.append(self)
 
    def mostrar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f' Restaurante: {restaurante.nome} \n Categoria: {restaurante.categoria} \n Ativo: {restaurante.ativo} \n Avaliacao: {restaurante.avaliacao} \n Rodizio: {restaurante.rodizio}')

Restaurante01 = Restaurante('Terraço Itália', 'Italiano', '⭐⭐⭐⭐⭐', 'Não')
Restaurante.mostrar_restaurantes()
        