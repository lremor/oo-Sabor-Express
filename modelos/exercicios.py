# 01. Classes

# Exercicio atributos de uma classe

# class Musica:
#     artista = ''
#     nome = ''
#     duracao = ''

# musica = Musica()
# musica.artista = 'Linkin Park'
# musica.nome = 'In the end'
# musica.duracao = '3:00'

# print(f'banda: {musica.artista}\nnome: {musica.nome}\nduracao: {musica.duracao}')

# Exercicio 01 ao 09

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'
categoria = Restaurante.categoria

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

if restaurante_praca.ativo == False:
    print(f'restaurante: {restaurante_praca.nome}\ncategoria: {restaurante_praca.categoria}\nativo: não')
else:
    print(f'restaurante: {restaurante_praca.nome}\ncategoria: {restaurante_praca.categoria}\nativo: sim')

if restaurante_pizza.ativo == False:
    print(f'restaurante: {restaurante_pizza.nome}\ncategoria: {restaurante_pizza.categoria}\nativo: não')
else:
    print(f'restaurante: {restaurante_pizza.nome}\ncategoria: {restaurante_pizza.categoria}\nativo: sim')