import os
from pathlib import Path
from typing import Self
import tomllib

class Place:
    
    def __init__(
            self,
            name: str,
            description: str
        ) -> None:
        
        self._name = name
        self._description = description
    
    @property
    def name(self) -> str:
        """Place name.
        """
        
        return self._name
    
    @property
    def description(self) -> str:
        """A brief description about the place.
        """

        return self._description
    
    @classmethod
    def from_toml(cls, filepath: os.PathLike) -> Self:
        """Load place from TOML.

        Parameters
        ----------
            filepath (os.PathLike): TOML configuration file.

        Returns
        -------
            Self: Place.
        """
        
        # load data from TOML
        filepath = Path(filepath)
        with open(filepath, 'rb') as f:
            data = tomllib.load(f)
        
        # create place instance
        assert set(['name', 'description']).issubset(data.keys())
        return cls(
            name=data['name'], 
            description=data['description']
        )

    