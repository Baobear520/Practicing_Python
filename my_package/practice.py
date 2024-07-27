class Player:
    def __init__(self):
        self._height = 160
        self._weight = 60

    @property
    def height(self):
        return self._height
    
    @property
    def weight(self):
        return self._weight
    
    @height.setter
    def height(self,value):
        if value < 0 or value > 250:
            raise ValueError("Incorrect value")
        
    @weight.setter
    def weight(self,value):
        if 200 < value or value < 30:
            raise ValueError("Incorrect value") 

    @property
    def bmi(self):
        return round(((self.height-100)/self.weight),2)
    
    def __str__(self):
        return f"My height is {self.height} and weight is {self.weight}"


steph = Player()
steph.number_of_rings = 4
print(id(steph))
print(steph.number_of_rings)
print(id(steph))

steph.height = -1





