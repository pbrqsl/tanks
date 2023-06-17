from dataclasses import dataclass
from datetime import datetime
from tanks.tank import Tank


@dataclass
class Operation:
    tank_id: str
    name: str
    volume: int
    result: bool
    timestamp: datetime


class OperationAnalyzer:
    @classmethod
    def analyze_tank_operations(cls, tank_id: str, operations: list[Operation]) -> int:
        current = 0
        for operation in operations:
            if operation.tank_id == tank_id and operation.result:
                if operation.name == "pour_in" or operation.name == "transfer_water":
                    current += operation.volume

                elif operation.name == "pour_out":
                    current -= operation.volume

        return current
