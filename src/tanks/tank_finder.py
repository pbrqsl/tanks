from typing import List

from operations.operation import Operation
from tanks.tank import Tank


class TankFinder:
    def __init__(self, tanks: list[Tank]):
        self.tanks = tanks

    def max_water(self) -> Tank:
        if self.tanks:
            max_water_tank = self.tanks[0]
            for tank in self.tanks[1:]:
                if tank.current > max_water_tank.current:
                    max_water_tank = tank
            return max_water_tank

    def most_filled(self) -> Tank:
        if self.tanks:
            most_filled_tank = self.tanks[0]
            for tank in self.tanks[1:]:
                if tank.water_level > most_filled_tank.water_level:
                    most_filled_tank = tank
            return most_filled_tank

    def empty_tanks(self) -> list[Tank]:
        empty_tanks = []
        for tank in self.tanks:
            if tank.current == 0:
                empty_tanks.append(tank)
        return empty_tanks
