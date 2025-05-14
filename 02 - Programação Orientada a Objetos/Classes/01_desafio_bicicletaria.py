class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=26 ):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    #DEFININDO MÉTODOS
    def buzinar(self):
        print("Buzinando!")
    
    def parar(self):
        print("Parando!")
        print("Bicicleta parada!")

    def correr(self):
        print("Correndo!")

    #def __str__(self):
     #   return f"Bicicleta {self.modelo} de cor {self.cor} do ano {self.ano} está saindo pelo valor de R$ {self.valor},00."
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', ' .join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" #Dessa forma, não preciasamos definir o __str__ para cada classe, pois ele já vai pegar todos os atributos da classe e imprimir no formato desejado.

b1 = Bicicleta("azul", "caloi", 2020, 500)
b1.correr()
b1.buzinar()
b1.parar()
print(b1.ano)

b2 = Bicicleta("amarela", "monark", 2001, 254)
Bicicleta.parar(b2) # = b2.parar()

print(b2)

