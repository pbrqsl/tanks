from operations.operation import Operation
from tanks.tank import Tank


class EventSourcer:
    def __init__(self):
        self.operations: list[Operation] = []

    def find_most_unsuccessfull(self) -> Tank:
        tank_directory = {}
        most_unsuccessful_tank = None
        for operation in self.operations:
            if not operation.result:
                if tank_directory.get(operation.tank_id):
                    tank_directory[operation.tank_id] += 1
                else:
                    tank_directory[operation.tank_id] = 1

        if tank_directory:
            most_unsuccessful_tank = max(
                zip(tank_directory.values(), tank_directory.keys())
            )[1]
            return most_unsuccessful_tank
        return None

    def find_most_of_type(self, type: str):
        tank_directory = {}
        most_of_type_tank = None
        for operation in self.operations:
            if operation.name == type:
                if tank_directory.get(operation.tank_id):
                    tank_directory[operation.tank_id] += 1
                else:
                    tank_directory[operation.tank_id] = 1
        if tank_directory:
            most_of_type_tank = max(
                zip(tank_directory.values(), tank_directory.keys())
            )[1]
            return most_of_type_tank
        return None
