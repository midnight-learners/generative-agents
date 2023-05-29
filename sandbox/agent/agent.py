from xpyutils import lazy_property
from ..env import Place

class Agent:
    
    def __init__(
            self,
            name: str,
        ) -> None:
        
        self._name = name
    
    @property
    def name(self) -> str:
        """Agent name.
        """
        
        return self._name
    
    @property
    def place(self) -> Place:
        
        ...
    