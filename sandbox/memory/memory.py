from typing import Self
from enum import Enum
from datetime import datetime

class MemoryType(Enum):
    
    Observation = 1
    Reflection = 2
    Plan = 3
    
    def from_int(type_code: int) -> Self:
        
        if type_code == 1:
            return MemoryType.Observation
        elif type_code == 2:
            return MemoryType.Reflection
        elif type_code == 3:
            return MemoryType.Plan
        else:
            raise ValueError('Type code can only be 1, 2 or 3')

class Memory:
    
    def __init__(
            self,
            content: str,
            date_time: datetime = datetime.now(),
            type: MemoryType = MemoryType.Observation
        ) -> None:
        
        self._content = content
        self._date_time = date_time
        self._type = type
    
    def __str__(self) -> str:
        
        return f"[{self.type.name}] {self.date_time.strftime('%F %T')} {self.content}"
    
    def __repr__(self) -> str:
        
        return self.__str__()
    
    @property
    def content(self) -> str:
        """Memory content.
        """
        
        return self._content
    
    @property
    def date_time(self) -> datetime:
        """Date and time when the memory is created.
        """
        
        return self._date_time
    
    @property
    def type(self) -> MemoryType:
        """Type of the memory. 
        It can be an observaton, reflection or plan.
        """
        
        return self._type