
from copy import deepcopy


try:
    from dz4.linked_list import Node
except ImportError:
    from linked_list import Node    

from linked_list import Linked_list

class Linked_list_tweaked(Linked_list):
    def pop_last(self) -> Node:
        if len(self) >1:
            return super().pop_last()
        "Выдёргиваем последний элемент"
        if self.head:
            tmp = deepcopy(self.tail)
            self.tail = self.head
            self.head = None
            return tmp
    
    def __bool__(self) -> bool:
        return True if self.head is not None else False