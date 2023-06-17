from tanks.tank import Tank
from operations.operation import Operation
from tanks.tank_finder import TankFinder
from sourcers.eventsourcer import EventSourcer
from operations.operation import OperationAnalyzer
from datetime import datetime


class Manager:
    def __init__(self):
        self.tanks: list[Tank] = []
        self.tankfinder = TankFinder(self.tanks)
        self.sourcer = EventSourcer()
        self.analyzer = OperationAnalyzer()

    def pour_in_water(self, tank: Tank, volume: int) -> None:
        operation_result = tank.pour_in_water(volume)
        self.sourcer.operations.append(
            Operation(
                tank_id=tank.id,
                name="pour_in",
                volume=volume,
                result=operation_result,
                timestamp=datetime.now(),
            )
        )

    def pour_out_water(self, tank: Tank, volume: int) -> None:
        operation_result = tank.pour_out_water(volume)
        self.sourcer.operations.append(
            Operation(
                tank_id=tank.id,
                name="pour_out",
                volume=volume,
                result=operation_result,
                timestamp=datetime.now(),
            )
        )

    def transfer_water(self, tank_from: Tank, tank_to: Tank, volume: int) -> None:
        operation_result = tank_to.transfer_water(tank_from=tank_from, volume=volume)
        self.sourcer.operations.extend(
            [
                Operation(
                    tank_id=tank_to.id,
                    name="transfer_water",
                    volume=volume,
                    result=operation_result,
                    timestamp=datetime.now(),
                ),
                Operation(
                    tank_id=tank_from.id,
                    name="pour_out",
                    volume=volume,
                    result=operation_result,
                    timestamp=datetime.now(),
                ),
            ]
        )

    def analyze_tank(self, tank: Tank):
        analyzer_current = self.analyzer.analyze_tank_operations(
            tank.id, self.sourcer.operations
        )
        if tank.current == analyzer_current:
            return True
        return False
