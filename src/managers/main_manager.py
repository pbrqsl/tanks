from tanks.tank import Tank
from operations.operation import Operation


class Manager:
    def __init__(self):
        self.tanks: list[Tank] = []
        self.operations: list[Operation] = []

    def pour_in_water(self, tank: Tank, volume: int):
        if self._is_enough_capacity(tank, volume):
            tank.pour_in_water(volume)
            self.operations.append(
                Operation(
                    tank_ID=tank.ID,
                    operation_name="pour_in",
                    volume=volume,
                    result=True,
                )
            )
        else:
            self.operations.append(
                Operation(
                    tank_ID=tank.ID,
                    operation_name="pour_in",
                    volume=volume,
                    result=False,
                )
            )

    def pour_out_water(self, tank: Tank, volume: int):
        if self._is_enough_water(tank, volume):
            tank.pour_out_water(volume)
            self.operations.append(
                Operation(
                    tank_ID=tank.ID,
                    operation_name="pour_out",
                    volume=volume,
                    result=True,
                )
            )
        else:
            self.operations.append(
                Operation(
                    tank_ID=tank.ID,
                    operation_name="pour_out",
                    volume=volume,
                    result=False,
                )
            )

    def _is_enough_water(self, tank: Tank, water: int):
        if tank.current >= water:
            return True
        return False

    def _is_enough_capacity(self, tank: Tank, water):
        if tank.free_capacity >= water:
            return True
        return False
