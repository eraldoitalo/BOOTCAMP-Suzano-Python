class Person:
    def __init__(self, name, year_birth):
        self._name = name 
        self._year_birth = year_birth

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        _current_year = 2025
        return _current_year - self._year_birth
    
Pessoa = Person("Italo", 2003)
print(f"Name: {Pessoa.name} \tAge: {Pessoa.age}")
    
    