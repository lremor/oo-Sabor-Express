from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia',5.0,'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_sagu = Sobremesa('Sagu',1.50,'A melhor sobremesa','Muito doce','Grande')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_sagu)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()


