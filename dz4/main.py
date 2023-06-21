from enum import Enum, auto
"""
Необходимо превратить собранное на семинаре дерево поиска в полноценное
левостороннее красно-черное дерево.
И реализовать в нем метод добавления новых элементов с балансировкой.

Красно-черное дерево имеет следующие критерии:
• Каждая нода имеет цвет (красный или черный)
• Корень дерева всегда черный
• Новая нода всегда красная
• Красные ноды могут быть только левым ребенком
• У краной ноды все дети черного цвета

Соответственно, чтобы данные условия выполнялись, 
после добавления элемента в дерево необходимо произвести балансировку, 
благодаря которой все критерии выше станут валидными. 
Для балансировки существует 3 операции – 
* левый малый поворот,
* правый малый поворот
* и смена цвета.
"""

from datetime import datetime
from copy import deepcopy
class Color(Enum):
    """цвет"""
    RED = auto()
    BLACK = auto()


class Node():
    """Нода. """
    def __init__(self,
                 value_i:int = None,
                 left_child_i:'Node' = None,
                 right_child_i:'Node' = None,
                 color_i:Color = Color.RED):
        self.__value = value_i
        self.left_child = left_child_i
        self.right_child = right_child_i
        self.color = color_i
        self.__create_date = datetime.now().timestamp

    def set(self,new_int:int):
        if isinstance(new_int,int):
            self.__value= new_int
        else:
            print("Not changed. Int expected.")
    
    def get(self):
        return self.__value

    def __str__(self):
        return f"{self.color.name} Node with value {self.get()}"
            # рекурсивно выводим детей.. громоздко и не нужно
            # + f' {f" Left child: {str(self.left_child)}" if self.left_child else ""}' \
            # + f'{f" Right child: {str(self.right_child)}" if self.right_child else ""}' 

    def __hash__(self) -> int:
        return hash(f"{self.__create_date}"\
                    + f"_{str(self.left_child)}_{str(self.right_child)}_"\
                    + f"{self.__value}")
    
    def __eq__(self, other_node: 'Node') -> bool:
        return hash(self) == hash(other_node)


class RedBlackTree():
    def __init__(self, root_node:Node) -> None:
        self.root = root_node
    
    def balance(self):
        raise NotImplementedError
    
    def add(self):
        raise NotImplementedError
    


def main():
    a = Node(3,None,None,Color.RED)
    b = Node(3,None,None,Color.RED)
    c = a
    d = deepcopy(a)
    e = deepcopy(a)
    e.left_child = b
    print(f"ab:{a==b}")
    print(f"ac:{a==c}")
    print(f"ad:{a==d}")
    print(f"ae:{a==e}")

if __name__ == "__main__":
    main()