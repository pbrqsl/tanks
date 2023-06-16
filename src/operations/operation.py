from dataclasses import dataclass
from datetime import datetime



@dataclass
class Operation:
    tank_id: str
    name: str
    volume: int
    result: bool
    timestamp: datetime
    



class OperationAnalyzer:
    pass
