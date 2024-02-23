from exercicios import Veiculo

class Moto(Veiculo):
    def __init__(self,classe,modelo,tipo):
        super().__init__(classe,modelo)
        self.tipo = tipo

   
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'Marca: {self.classe} | Modelo: {self.modelo} | Estado: {status} | Tipo: {self.tipo}'

