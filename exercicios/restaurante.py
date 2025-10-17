# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
# Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante():
    restaurantes = []

    def __init__(self, nome, categoria, ativo, avaliacao, rodizio):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacao = avaliacao
        self.rodizio = rodizio
        Restaurante.restaurantes.append(self)
 
    def mostrar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} \n {restaurante.categoria} \n {restaurante.ativo} \n {restaurante.avaliacao} \n {restaurante.rodizio}')

Restaurante01 = Restaurante('Terraço Itália', 'Italiano', 'Sim', '⭐⭐⭐⭐⭐', 'Não')
Restaurante.mostrar_restaurantes()
        