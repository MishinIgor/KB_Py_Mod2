class Car:
    def __init__(self,model,power,mxspeed):
        self.model, self.power, self.mxspeed = model, power, mxspeed
        self.bak = 50
    def zapravka(self):
        print('Необходимо заправиться топливом')
class ElectroCar(Car):
    def __init__(self, model, power, mxspeed):
        super().__init__(model, power, mxspeed)
        self.batari = 100
    def zapravka(self):
        print('Необходима подзарядка')
Lada = Car('Westa',106,200)
Tesla = ElectroCar('TeslaN',150,200)
Lada.bak = 200
Tesla.bak = 150
print(Tesla.batari,Lada.bak)
Lada.zapravka()
Tesla.zapravka()