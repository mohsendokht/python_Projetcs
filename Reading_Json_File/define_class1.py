from dataclasses import dataclass
from typing import Tuple

@dataclass
class person():
      name: str = ''
      address: str = ''
      coordinates: Tuple = (0,0)
      
      def __repr__(self) -> str:
            return(f'The {self.__class__.__name__} is {self.name} and lives in {self.address}.')
            
p1 = person('Hamid1','London')   
p2 = person('Hamid','dunstable',(1,120))
print (p2)   