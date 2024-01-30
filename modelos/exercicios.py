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

#----------------------------------------

# Exercicio 01 ao 09

#----------------------------------------

# class Restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False

# restaurante_praca = Restaurante()
# restaurante_praca.nome = 'Bistrô'
# restaurante_praca.categoria = 'Italiana'
# categoria = Restaurante.categoria

# restaurante_pizza = Restaurante()
# restaurante_pizza.nome = 'Pizza Place'
# restaurante_pizza.categoria = 'Fast Food'
# restaurante_pizza.ativo = True

# if restaurante_praca.ativo == False:
#     print(f'restaurante: {restaurante_praca.nome}\ncategoria: {restaurante_praca.categoria}\nativo: não')
# else:
#     print(f'restaurante: {restaurante_praca.nome}\ncategoria: {restaurante_praca.categoria}\nativo: sim')

# if restaurante_pizza.ativo == False:
#     print(f'restaurante: {restaurante_pizza.nome}\ncategoria: {restaurante_pizza.categoria}\nativo: não')
# else:
#     print(f'restaurante: {restaurante_pizza.nome}\ncategoria: {restaurante_pizza.categoria}\nativo: sim')

#----------------------------------------
# 02. Construtor


class Musica:

    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def listar_musicas():
        print('---------------------------------------------')
        print('------------------MUSICAS--------------------')
        print('---------------------------------------------')
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao='2:48')
musica1 = Musica(nome='The Trooper', artista='Iron Maiden', duracao='2:45')
musica2 = Musica(nome='Hotel California', artista='Eagles', duracao='3:30')

Musica.listar_musicas()

#----------------------------------------

# Exercicios 01 ao 05

#----------------------------------------

class Carro:
    def __init__(self, modelo='', cor='', ano=''):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro = Carro(modelo='Golf GTI', cor='Prata', ano='2015')
print('---------------------------------------------')
print('------------------CARROS---------------------')
print('---------------------------------------------')
print(f'{carro.modelo} | {carro.cor} | {carro.ano}')



class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, promocao, fit):
        self.nome = nome
        self.categoria = categoria
        self.promocao = promocao
        self.fit = fit
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.promocao} | {self.fit}'

    def listar_restaurantes():
        print('---------------------------------------------')
        print('----------------RESTAURANTES-----------------')
        print('---------------------------------------------')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.promocao} | {restaurante.fit} | {restaurante.ativo}')
                  
restaurante_praca = Restaurante('Rakki', 'Sushi', 'Não', 'Sim')
restaurante_pizza = Restaurante('Alto Uruguai', 'Pizzaria', 'Sim', 'Não' )

Restaurante.listar_restaurantes()

class Clientes:

    clientes = []

    def __init__(self, nome, cpf, endereco, sexo):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.sexo = sexo
        Clientes.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.cpf} | {self.endereco} | {self.sexo}'
    
    def listar_clientes():
        print('---------------------------------------------')
        print('------------------CLIENTES-------------------')
        print('---------------------------------------------')
        for cliente in Clientes.clientes:
            print(f'{cliente.nome} | {cliente.cpf} | {cliente.endereco} | {cliente.sexo}')

clientes_1 = Clientes('Luis', '87676534509', 'Rua São Paulo', 'Masculino')
clientes_2 = Clientes('Liana', '84276523500', 'Avenida Sete de Setembro', 'Feminino')
clientes_3 = Clientes('Rita', '13665334504', 'Rua Goias', 'Feminino')

Clientes.listar_clientes()