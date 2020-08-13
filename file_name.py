class Dog():
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color

dog = Dog('Fido','Brown')

print(dog.name)
print(dog.color)