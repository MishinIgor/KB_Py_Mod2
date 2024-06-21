class Car:
    kolesa = 4
    fara = 2
    rul = 1
    def __init__(self,marka,color,maxspeed,earinput):
        self.marka = marka
        self.color = color
        self.maxspeed = maxspeed
        self.earinput = earinput
    def ezda(self,speed,distance):
        if int(self.maxspeed) < int(speed):
            return 'Машина сломалась'
        else:
            time = distance/speed
            if time > 1:
                vibor = input('Введите +, если хотите перевести в минуты, ++ если в секунды, - если оставить так: ')
                if vibor == '+':
                    return time * 60
                elif vibor == '++':
                    return time * 3600
            else:
                return time

        
        
    