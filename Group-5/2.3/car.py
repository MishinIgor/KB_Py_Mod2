class car:
    def __init__(self,model,color,maxspeed):
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
    def outinfo(self):
        return f'Модель: {self.model}, цвет: {self.color}, Максимальная скорость: {self.maxspeed} км/ч'
    def timemove(self,speed,distance):
        if speed > self.maxspeed:
            return f'Машина сломалась, превышена скорость на: {speed - self.maxspeed}'
        else:
            return distance/speed
    
        
        