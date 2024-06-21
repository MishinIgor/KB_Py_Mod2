class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")
    def schet(x,y):
        print(x+y)
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Dog barks")
Cat = Animal('Матроскин')
Pes = Dog('Шарик')
Cat.speak()
Pes.speak()
print(Cat.name)
print(Pes.name)