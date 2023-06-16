from tanks.tank import Tank
from typing import List

class TankFinder:
    def __init__(self, tanks: list[Tank]):
        self.tanks = tanks
        
    def max_water(self):
        if self.tanks:
            max_water_tank = self.tanks[0]
            for tank in self.tanks[1:]:
                if tank.current > max_water_tank.current:
                    max_water_tank = tank
            return max_water_tank