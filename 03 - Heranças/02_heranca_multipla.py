class Animal:
    def __init__(self, paws):
        self.paws = paws

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class Mammal(Animal):
    def __init__(self, color_fur, **kw):
        self.color_fur = color_fur
        super().__init__(**kw)

class Bird(Animal):
    def __init__(self, color_beak, **kw):
        self.color_baek = color_beak
        super().__init__(**kw)

class Cat(Mammal):
    pass

class Ornithorhynchus (Mammal, Bird):
    def __init__(self, color_beak, color_fur, paws):
        super().__init__(color_beak=color_beak, color_fur=color_fur, paws=paws)

cat = Cat(paws=4, color_fur="black")
print(cat)

ornithorhynchus = Ornithorhynchus(paws=2, color_fur="brown", color_beak="orange")
print(ornithorhynchus)