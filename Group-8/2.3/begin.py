class Dog:
    ushi = True
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def outinfo(self):
        return f'Имя: {self.name} Возраст: {self.age}'
    def speak(self,sound):
        return f'{self.name} сказал {sound}'


