from tools.namegenerator import NameGenerator


class Tank:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0
        self.id = NameGenerator.random_name()

    def __repr__(self):
        return f"<Tank: id={self.id} current={self.current}>"

    def pour_in_water(self, volume: int) -> bool:
        if self.free_capacity >= volume:
            self.current += volume
            return True
        return False

    def pour_out_water(self, volume: int) -> bool:
        if self.current >= volume:
            self.current -= volume
            return True
        return False

    def transfer_water(self, tank_from: "Tank", volume) -> bool:
        if self != tank_from and self.free_capacity >= volume:
            if tank_from.current >= volume:
                self.pour_in_water(volume=volume)
                tank_from.pour_out_water(volume=volume)
                return True
            return False
        return False

    @property
    def free_capacity(self) -> int:
        return self.capacity - self.current

    @property
    def water_level(self) -> float:
        return self.current / self.capacity
