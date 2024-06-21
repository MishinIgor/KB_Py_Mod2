class Hleb:
    zapah = 'Божественный'
    def __init__(self,model,color,m):
        self.model = model
        self.color = color
        self.m = m
    def outinfo(self):
        return f'Название хлеба: {self.model}, цвет хлеба: {self.color}, масса: {self.m}'
    def perevod(self):
        return self.m/1000
    def ingridient(self):
        return f'Нужно муки: {0.6*self.m}, Воды нужно: {0.3*self.m}, соль, перец и начинка: {0.1*self.m}'
        
        