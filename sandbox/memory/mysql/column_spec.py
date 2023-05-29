from typing import Self, Any
from enum import Enum

class MySQLColumnKey(Enum):
    
    NULL = 0
    
    PRI = 1
    UNI = 2
    MUL = 3
    
    @classmethod
    def from_str(cls, key_str: str) -> Self:
        
        # convert to upper case
        key_str = key_str.upper()
        
        # primary key
        if key_str in {'PRI', 'PRIMARY', 'PRIMARY KEY'}:
            return MySQLColumnKey.PRI
        
        # unique key
        elif key_str in {'UNI', 'UNIQUE', 'UNIQUE KEY'}:
            return MySQLColumnKey.UNI
        
        # multiple key
        elif key_str in {'MUL', 'MULTIPLE', 'MULTIPLE KEY'}:
            return MySQLColumnKey.MUL
        
        # the key is not set
        else:
            return MySQLColumnKey.NULL

class MySQLColumnSpec:
    """Column specification of a table.
    """
    
    def __init__(
            self,
            field: str,
            type: str,
            null: bool | str = False,
            key: MySQLColumnKey | str = '',
            default: Any = None,
            extra: str = ''
        ) -> None:
        
        self._field = field
        self._type = type
        
        # set up null
        
        # set up null from str
        if isinstance(null, str):
            
            # convert to lower case
            null = null.lower()
            
            if null in {'y', 'yes'}:
                self._null = True
            
            else:
                self._null = False
        
        else:
            assert isinstance(null, bool), "parameter 'null' can either be str or bool"
            self._null = null

        # set up key specification
        self._key = MySQLColumnKey.from_str(key)
        
        self._default = default
        self._extra = extra
    
    @property
    def field(self) -> str:
        """Field name.
        """
        
        return self._field
    
    @property
    def type(self) -> str:
        """Data type of this column.
        """
        
        return self._type
    
    @property
    def null(self) -> bool:
        """Whether the value of this column can be null/None.
        """
        
        return self._null
    
    @property
    def key(self) -> MySQLColumnKey:
        """Key specification of the column.
        """
        
        return self._key
    
    @property
    def default(self) -> Any:
        """Default value of the column
        when a new record is inserted into database
        without specifying this column.
        """
        
        return self._default
    
    @property
    def extra(self) -> str:
        """Extra information.
        """
        
        return self._extra
    
    def is_primary_key(self) -> bool:
        """Whether the column is defined with a primary key.
        """
        
        return self.key == MySQLColumnKey.PRI
    
    