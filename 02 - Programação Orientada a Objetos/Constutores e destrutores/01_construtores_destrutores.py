class Cachorro:
    def __init__(self, nome, cor, acordado=True): #construtor __init__
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado 

    def __del__(self):
        print("Removendo a instancia da classe.")

    def latir(self): #destrutor __del__ 
        print("auau")

dog = Cachorro("Toby", "Marrom")
dog.latir()

print("ola mundo")
print("ola mundo")
del dog  
print("ola mundo")
print("ola mundo")