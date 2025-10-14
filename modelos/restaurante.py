class restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

#print(restaurante_praca) -> exibição da alocação na memória
#print(dir(restaurante_praca)) -> todas informações do objeto
#print(vars(restaurante_praca)) -> exibição do conteúdo da classe em um dicionário

#print(restaurante_praca.ativo) -> exibição de um objeto expecífico
