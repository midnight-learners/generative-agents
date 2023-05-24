from xpyutils import lazy_property
from ..location import Location

class Agent:
    
    def __init__(
            self,
            name: str,
        ) -> None:
        
        self._name = name
    
    @lazy_property.require_presence()
    def name(self) -> str:
        """Agent name.
        """
        
        return self._name
    
    @property
    def location(self) -> Location:
        
        ...
    