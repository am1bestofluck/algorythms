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
from random import choice, sample


from linked_list import Linked_list, Node as ll_node

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
        self.__color = color_i
        self.__create_date = datetime.now().timestamp

    def set_value(self,new_int:int):
        if isinstance(new_int,int):
            self.__value= new_int
        else:
            print("Not changed. Int expected.")
    
    def get_value(self):
        return self.__value
    
    def set_color(self,new_color:Color):
        if isinstance(new_color,Color):
            self.__color = new_color
        else:
            print("Not changed. Enum `Color` expected.")

    def __str__(self):
        return f"{self.__color.name} Node with value {self.__value}"
            # рекурсивно выводим детей.. громоздко и не нужно
            # + f' {f" Left child: {str(self.left_child)}" if self.left_child else ""}' \
            # + f'{f" Right child: {str(self.right_child)}" if self.right_child else ""}' 

    def __hash__(self) -> int:
        return hash(f"{self.__create_date}"\
                    + f"_{str(self.left_child)}_{str(self.right_child)}_"\
                    + f"{self.__value}"\
                    + f"{self.__color.name}")
    
    def __eq__(self, other_node: 'Node') -> bool:
        return hash(self) == hash(other_node)

    def __gt__(self,other_node:'Node'):
        return self.__value > other_node.get_value()

class RedBlackTree():
    "собственно дерево"
    def __init__(self, root_node:Node) -> None:
        self.root = root_node
        root_node =
    
    def balance(self):
        raise NotImplementedError
    
    def add(self):
        raise NotImplementedError
    
    def remove(self):
        raise NotImplementedError
    
    def __str__(self):
        return """Tree."""

def check_eq():
    """к задаче не относится, тестирую дандеры"""
    a = Node(3,None,None,Color.RED)
    b = Node(3,None,None,Color.RED)
    c = a
    d = deepcopy(a)
    e = deepcopy(a)
    f = deepcopy(a)
    f.set_color(Color.BLACK)
    e.left_child = b
    assert a != b
    assert a == c
    assert a == d
    assert a != f
    assert a != e
    print('ok!')

def compareNodes():
    """к задаче не относится, тестирую другие дандеры"""
    eq_a = Node(1,None,None,Color.RED)
    eq_b = Node(1, None, None, Color.BLACK)
    l_c = Node(0,eq_a,eq_b,Color.RED)
    b_dd = Node(2,None,None,Color.BLACK)
    assert eq_a > l_c
    assert eq_b < b_dd
    print('ok!')

def main():
    values = sample(range(1000),k = 10)
    queue = Linked_list(ll_node(values[0]))
    for i in values[1:]:
        queue.add_first(ll_node(i))
    RBT = RedBlackTree(Node(queue.pop_last().get()))
    print(RBT.root)
    print(RBT)

if __name__ == "__main__":
    main()