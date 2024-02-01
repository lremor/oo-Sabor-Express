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


# class Musica:

#     musicas = []

#     def __init__(self, nome, artista, duracao):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao
#         Musica.musicas.append(self)

#     def listar_musicas():
#         print()
#         print('---------------------------------------------')
#         print('------------------MUSICAS--------------------')
#         print('---------------------------------------------')
#         print(f'{'Musica'.ljust(25)} | {'Artista'.ljust(25)} | {'Duração'}')
#         print('----------------------------------------------------------------')
#         for musica in Musica.musicas:
#             print(f'{musica.nome.ljust(25)} | {musica.artista.ljust(25)} | {musica.duracao}')

# musica = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao='2:48')
# musica1 = Musica(nome='The Trooper', artista='Iron Maiden', duracao='2:45')
# musica2 = Musica(nome='Hotel California', artista='Eagles', duracao='3:30')

# Musica.listar_musicas()

#----------------------------------------

# Exercicios 01 ao 05

#----------------------------------------

# class Carro:
#     def __init__(self, modelo='', cor='', ano=''):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano

# carro = Carro(modelo='Golf GTI', cor='Prata', ano='2015')
# print()
# print('---------------------------------------------')
# print('------------------CARROS---------------------')
# print('---------------------------------------------')
# print(f'{'Modelo'.ljust(25)} | {'Cor'.ljust(25)} | {'Ano'}')
# print('------------------------------------------------------------')
# print(f'{carro.modelo.ljust(25)} | {carro.cor.ljust(25)} | {carro.ano.ljust(25)}')



# class Restaurante:
#     restaurantes = []

#     def __init__(self, nome, categoria, promocao, fit):
#         self.nome = nome
#         self.categoria = categoria
#         self.promocao = promocao
#         self.fit = fit
#         self.ativo = False
#         Restaurante.restaurantes.append(self)

#     def __str__(self):
#         return f'{self.nome} | {self.categoria} | {self.promocao} | {self.fit}'

#     def listar_restaurantes():
#         print()
#         print('---------------------------------------------')
#         print('----------------RESTAURANTES-----------------')
#         print('---------------------------------------------')
#         print(f'{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Promoção'.ljust(25)} | {'Fit'.ljust(25)} | {'Ativo'.ljust(25)}')
#         print('---------------------------------------------------------------------------------------------------------------------')
#         for restaurante in Restaurante.restaurantes:
#             print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.promocao.ljust(25)} | {restaurante.fit.ljust(25)} | {restaurante.ativo}')
                  
# restaurante_praca = Restaurante('Rakki', 'Sushi', 'Não', 'Sim')
# restaurante_pizza = Restaurante('Alto Uruguai', 'Pizzaria', 'Sim', 'Não' )

# Restaurante.listar_restaurantes()

# class Clientes:

#     clientes = []

#     def __init__(self, nome, cpf, endereco, sexo):
#         self.nome = nome
#         self.cpf = cpf
#         self.endereco = endereco
#         self.sexo = sexo
#         Clientes.clientes.append(self)

#     def __str__(self):
#         return f'{self.nome} | {self.cpf} | {self.endereco} | {self.sexo}'
    
#     def listar_clientes():
#         print()
#         print('---------------------------------------------')
#         print('-------------------CLIENTES------------------')
#         print('---------------------------------------------')
#         print(f'{'Cliente'.ljust(25)} | {'CPF'.ljust(25)} | {'Endereço'.ljust(25)} | {'Sexo'.ljust(25)}')
#         print('---------------------------------------------------------------------------------------------')
#         for cliente in Clientes.clientes:
#             print(f'{cliente.nome.ljust(25)} | {cliente.cpf.ljust(25)} | {cliente.endereco.ljust(25)} | {cliente.sexo}')

# clientes_1 = Clientes('Luis', '87676534509', 'Rua São Paulo', 'Masculino')
# clientes_2 = Clientes('Liana', '84276523500', 'Avenida Sete de Setembro', 'Feminino')
# clientes_3 = Clientes('Rita', '13665334504', 'Rua Goias', 'Feminino')

# Clientes.listar_clientes()


#----------------------------------------
# 03. Property

class Pessoa:

    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        if self.profissao:
            return f'{self.nome} | {self.idade} anos | {self.profissao}'
        else:
            return f'{self.nome} | {self.idade} anos | Sem profissão'
        
    @property
    def saudacao(self):
        if self.profissao:
            return f'Sou {self.nome}, trabalho como {self.profissao}'
        else:
            return f'Sou {self.nome}, sem profissão'
    
    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)