def perevod(m):
    return m/1000
def SilaHleba(a,m):
    return a*m
class Hleb:
    Zapah = 'Божественный'
    def __init__(self,name,color,m):
        self.name = name
        self.color = color
        self.m = m
    def vsesrazu(self):
        return f'Zapah: {self.Zapah} Name:{self.name} color: {self.color} m: {self.m} грамм'
