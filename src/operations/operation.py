class Operation:
    def __init__(self, tank_ID: str, operation_name: str, volume: int, result: bool):
        self.name = operation_name
        self.volume = volume
        self.result = result
        self.tank_ID = tank_ID

    def __repr__(self):
        return f"Operation({self.tank_ID}, {self.name}, {self.volume}, {self.result})"


class OperationAnalyzer:
    pass
