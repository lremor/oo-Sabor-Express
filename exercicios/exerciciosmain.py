from exercicios2 import Carro
from exercicios3 import Moto

carro1 = Carro('Audi', 'A3', 'Duas portas')
carro2 = Carro('Audi', 'A4', 'Quatro portas')
moto1 = Moto('CG','150','Casual')
moto2 = Moto('Yamaha','1000','Esportiva')

def main():
    print(carro1)
    print(carro2)
    Carro.ligar(moto1)
    print(moto1)
    print(moto2)

if __name__ == '__main__':
    main()