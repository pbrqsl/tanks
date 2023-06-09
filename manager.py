from tank import Tank

class Manager:
    def __init__(self):
        self.tanks: list[Tank] = []
    
    def pour_in_water(self, tank: Tank, water: int):
        if self._is_enough_capacity(tank, water):
            tank.current += water

    def pour_out_water(self, tank: Tank, water: int):
        if self._is_enough_water(tank, water):
            tank.current -= water

    def _is_enough_water(self, tank: Tank, water:int):
        if tank.current >= water:
            return True
        return False
    
    def _is_enough_capacity(self, tank: Tank, water):
        if tank.free_capacity >= water:
            return True
        return False
            
