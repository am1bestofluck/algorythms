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


from linked_list import Node as ll_node
from Linked_list_tweaked import Linked_list_tweaked as Linked_list

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
    
    def balance(self):
        """условный мэйн;
        балансируем дерево"""        
        raise NotImplementedError
    
    def __color_swap(Node):
            """красим детей если они `оба красные`?
              у нас тут левостороннее дерево, эта функция должна быть
              невостребованной"""
            raise NotImplementedError
    
    def __turn_left(Node):
        """разворачиваем локальный набор нод влево"""
        raise NotImplementedError
    
    def __turn_right(Node):
        """разворачиваем локальный набор нод вправо"""
        raise NotImplementedError
    
    def find( self, value:int, node_ir:Node) -> Node | None: # получилось :)
        """возвращаем ноду с этим значением
        или None если такой не нашлось
        проход в глубину
        """
        if node_ir.get_value() == value:
            return node_ir
        for child_ in [node_ir.left_child,node_ir.right_child]:
            try:
                result = self.find(value,child_)
            except AttributeError:
                result = None
            if result:
                return result
            
        return None
    def walk(self, node_ir:Node):
        """идём по нодам, читаем значения"""
        # в глубину  не фонтан
        """
        if node_ir == self.root:
            print("root: ", end = " ")
        if node_ir.get_value():
            print(node_ir.get_value())
        for child_ in [node_ir.left_child,node_ir.right_child]:
            try:
                if child_ == node_ir.left_child:
                    print( "left:",end = " ")
                    self.walk(child_)
                else:
                    print( "right:",end = " ")
                    self.walk(child_)
            except AttributeError:
                pass
            print()
        """
        floors=0

        current_line = list[Node]()
        current_line.append(self.root)
        
        while current_line:
            print(f"floor: {floors}")
            floors +=1
            for node_ in current_line:
                print(node_)
            next_line = list[Node]()
            if node_.left_child:
                next_line.append(node_.left_child)
            if node_.right_child:
                next_line.append(node_.right_child)
            current_line = next_line

        
    def add(self, node_: Node, new_value:int) -> bool:
        """добавляем ноду если такой нет -> true
        если такая есть  -> false"""
        if node_.get_value() == new_value:
            return False
        if node_.get_value() < new_value:
            if node_.right_child:
                result = self.add(node_.right_child,new_value)
                return result
            else:
                node_.right_child = Node(new_value)
                node_.right_child.set_color(Color.RED)
                return True
        else:
            if node_.left_child:
                result = self.add(node_.left_child,new_value)
                return result
            else:
                node_.left_child = Node(new_value)
                node_.left_child.set_color(Color.RED)
                return True
        
    def remove(self) -> bool:
        """удаляем ноду если она есть -> true
        если такой не нашлось -> false
        разобраться с детьми"""
        raise NotImplementedError
    
    def size(self): # получилось ^^
        """проходим по дереву, считаем сколько нод,
          и если получится - сколько этажей
          проход в ширину"""
        
        out = {
            "floors":0,
            "nodes":0
        }
        current_line = list[Node]()
        current_line.append(self.root)
        
        while current_line:
            out['floors'] +=1
            for node_ in current_line:
                out['nodes'] +=1
            next_line = list[Node]()
            if node_.left_child:
                next_line.append(node_.left_child)
            if node_.right_child:
                next_line.append(node_.right_child)
            current_line = next_line
        return out
    def __str__(self):
        tmp = self.size()
        return f"""Tree with root {str(self.root)};\n"""\
            + f"Has {tmp['floors']} floors and {tmp['nodes']} nodes."

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
    values = sample(range(1000),k = 10) # range(10)
    queue = Linked_list(ll_node(values[0]))
    for i in values[1:]:
        print(i)
        queue.add_first(ll_node(i))
    RBT = RedBlackTree(Node(queue.pop_last().get()))
    while queue:
        RBT.add(RBT.root,queue.pop_last().get())
    
    print(RBT)
    print(RBT.walk(RBT.root))
    print()

if __name__ == "__main__":
    main()