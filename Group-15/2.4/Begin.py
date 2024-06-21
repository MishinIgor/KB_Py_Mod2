class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self, name, m):
        super().__init__(name)
        self.m = m

    def speak(self):
        print("Dog barks")
Cat = Animal('Чижик')
Pes = Dog('Шарик',31)
print(Pes.m,Pes.name,Cat.name)
Cat.speak()
Pes.speak()