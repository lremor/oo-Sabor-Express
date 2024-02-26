# from exercicios2 import Carro
# from exercicios3 import Moto

# carro1 = Carro('Audi', 'A3', 'Duas portas')
# carro2 = Carro('Audi', 'A4', 'Quatro portas')
# moto1 = Moto('CG','150','Casual')
# moto2 = Moto('Yamaha','1000','Esportiva')

# def main():
#     print(carro1)
#     print(carro2)
#     Carro.ligar(moto1)
#     print(moto1)
#     print(moto2)

# if __name__ == '__main__':
#     main()

# 02. Polimorfismo
# Exercicios 01 ao 06

from exercicios2 import Carro

carro1 = Carro(classe="Ford", modelo="Focus", cor="Preto")
carro2 = Carro(classe="Chevrolet", modelo="Cruze", cor="Prata")
carro3 = Carro(classe="Honda", modelo="Civic", cor="Vermelho")
carro3.ligar()

def main():
    print(f"Carro 1: {carro1.classe} {carro1.modelo}, Cor: {carro1.cor}")
    print(f"Carro 2: {carro2.classe} {carro2.modelo}, Cor: {carro2.cor}")
    print(f"Carro 3: {carro3.classe} {carro3.modelo}, Cor: {carro3.cor}")

if __name__ == '__main__':
     main()