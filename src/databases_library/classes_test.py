
class Instance:

    def __init__(self,a: float,b: float):
        self.sum = a + b

class Multiple(Instance):

    def multi(self,x: int):
        return x*self.sum

flux = Multiple(a=2,b=3)

result = flux.multi(x=2)

print(f'\nk = {result}\n')

