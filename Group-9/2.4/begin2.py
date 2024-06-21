from begin import *
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Dog barks")

Pes = Dog('Шарик',3)
Cat = Animal('Матроскин')
Pes.speak()
Cat.speak()