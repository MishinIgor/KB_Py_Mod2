class Car:
    def __init__(self,model,color,maxspeed):
        self.model = model
        self.color = color
        self.maxspeed = float(maxspeed)
    def timemove(self,speed,distance):
        if speed > self.maxspeed:
            return 'Машина сломалась'
        else:
            return distance/speed
    def info(self):
        return f'Модель: {self.model}, Цвет: {self.color}, Максимальная скорость: {self.maxspeed} км/ч'
    def perevod(self):
        return f'{round(self.maxspeed*1000/3600,2)} м/c'
    
def perevodtime(time):
    return f'time ч. = {time * 3600} секунд'
        