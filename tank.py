from namegenerator import NameGenerator

class Tank():
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.current = 0
        self.ID = NameGenerator.random_name()
    def __repr__(self):
        return f'Tank: {self.ID}'
        
    
    @property
    def free_capacity(self):
        return self.capacity - self.current
    



class TankFinder():
    def max_water(self):
        pass