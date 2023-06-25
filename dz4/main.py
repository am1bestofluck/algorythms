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
• У красной ноды все дети черного цвета

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
                 color_i:Color = Color.RED,
                 parent_node:'Node' = None):
        self.__value = value_i
        self.left_child = left_child_i
        self.right_child = right_child_i
        self.__color = color_i
        self.parent = parent_node
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
    def get_color(self):
        return self.__color
    
    def __str__(self):
        return f"{self.__color.name}: {self.__value}_"\
            +f"(Root: {str(self.parent)})"
            # рекурсивно выводим детей.. громоздко и не нужно
            # + f' {f" Left child: {str(self.left_child)}" if self.left_child else ""}' \
            # + f'{f" Right child: {str(self.right_child)}" if self.right_child else ""}' 
    def __repr__(self):
        return f"{self.__color.name}: {self.__value}_"

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
    """собственно дерево"""
    def __init__(self, root_node:Node) -> None:
        self.root = root_node
        self.root.set_color(Color.BLACK)
    
    
    def __color_swap(self, node_x:Node) -> None:
        print("color swap")
        """красим детей если они `оба красные` - ситуация после правого поворота"""
        node_x.set_color( Color.RED)
        node_x.left_child.set_color(Color.BLACK)
        node_x.right_child.set_color(Color.BLACK)
        return node_x
    
    def __turn_right(self,node_x:Node) -> Node:
        """
         root                         root      
    |                            ||        
    x40        RightRotate(40)    20        
   //  \         --->          //   \      
  y20    v50                    10    40           
 //                                   \      
w10                                     50"""
        print("right turn")
        node_y = node_x.left_child
        node_x.left_child = node_y.right_child
        node_y.right_child = node_x
        node_y.set_color(node_x.get_color())
        node_x.set_color(Color.RED)
        return node_y
    
    def __turn_left(self,node_x:Node) -> Node:
        """разворачиваем локальный набор нод вправо, если мы добавляем ребёнка влево."""
        """
            root                        root     
        |                          ||      
        40      LeftRotate(40)     50     
        /  \\        --->          /  \    
    NULL  50                   40   NULL    
        """
        print("left turn")
        node_y = node_x.right_child
        node_x.right_child = node_x.left_child
        node_y.left_child = node_x
        node_x.set_color(Color.RED)
        node_y.set_color(Color.BLACK)
        return node_y
    
    
    def __balance(self,node_i:Node):
        """условный мэйн;
        балансируем дерево"""
        result = node_i
        # если есть левый а правого нет - балансируем влево
        """
          if self.is_red(root.right) and not self.is_red(root.left):
            root = self.rotate_left(root)
        if self.is_red(root.left) and self.is_red(root.left.left):
            root = self.rotate_right(root)
        if self.is_red(root.left) and self.is_red(root.right):
            self.flip_color(root)
        """
        if node_i.left_child is not None and node_i.right_child is not None:
            # swap
            if node_i.left_child.get_color() == Color.RED and\
                node_i.right_child.get_color() == Color.RED:
                node_i = self.__color_swap(node_i)
                pass
            # left turn
            elif node_i.left_child.get_color() == Color.BLACK and\
                node_i.right_child.get_color() == Color.RED:
                node_i = self.__turn_left(node_i)
                pass
            pass
        try:
            tmp1,tmp2 = node_i.left_child,node_i.left_child.left_child
            if tmp1.get_color() == Color.RED and tmp2.get_color() == Color.RED:
                node_i  = self.__turn_right(node_i)
        except AttributeError:
            pass #левый-левый нон
        return node_i

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
        floors=0
        current_line = list[Node]()
        current_line.append(self.root)
        while current_line:
            print(f"floor: {floors}")
            floors +=1
            next_line = list[Node]()
            for node_ in current_line:
                print(node_)
                if node_.left_child:
                    next_line.append(node_.left_child)
                if node_.right_child:
                    next_line.append(node_.right_child)
            current_line = next_line
    @staticmethod
    def is_red(node:Node) -> bool:
        if node is None:
            return False
        return node.get_color() == Color.RED

    def add(self,new_value) -> bool:
        self.root = self.__add(self.root, new_value)
        self.root.set_color(Color.BLACK)
    
    def __add(self,node_i:Node,new_value):
         
        if node_i is None:
            return Node(new_value)

        if new_value < node_i.get_value():
            node_i.left_child = self.__add(node_i.left_child, new_value)
        elif new_value > node_i.get_value():
            node_i.right_child = self.__add(node_i.right_child, new_value)
        else:
            node_i.set_value(new_value)
        
        if self.is_red(node_i.right_child) and\
                self.is_red(node_i.left_child):
            node_i = self.__color_swap(node_i)
    
    
        if self.is_red(node_i.right_child) and\
                not self.is_red(node_i.left_child):
            node_i = self.__turn_left(node_i)
        if self.is_red(node_i.left_child) and\
                self.is_red(node_i.left_child.left_child):
            node_i = self.__turn_right(node_i)
        return node_i

    
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
            next_line = list[Node]()
            for node_ in current_line:
                out['nodes'] +=1
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
    values = sample(range(100),k = 15)
    values = list(range(7))
    queue = Linked_list(ll_node(values[0]))
    for i in values[1:]:
        queue.add_first(ll_node(i))
    RBT = RedBlackTree(Node(queue.pop_last().get()))
    while queue:
        RBT.add(queue.pop_last().get())
    
    print(RBT)
    print(RBT.walk(RBT.root))

if __name__ == "__main__":
    main()