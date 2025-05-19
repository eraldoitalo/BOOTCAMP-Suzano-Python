class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade) # eu não preciso fazer a chamada da instacia da classe, pois o cls ja identifica que estou chamando Pessoa
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18 # dessa forma eu crio um metodo estatico
    
p = Pessoa.data_nascimento(2003, 6, 5, "Italo")
print(p.nome, p.idade)
print(Pessoa.maior_idade(22))