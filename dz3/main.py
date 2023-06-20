from datetime import datetime
from copy import deepcopy
"""Необходимо реализовать метод разворота связного списка 
(двухсвязного или односвязного на выбор)."""


class Node():

    """звено цепи, значение задаётся при ините
    сравнения могут вылететь если сравниваем разные типы...
    но для proof-of-concept столько должно хватить
    """

    def __init__(self, value: any):
        self.__create_date = datetime.now()
        self.__value = value
        self.next: Node = None
        self.prev: Node = None

    def set(self, newValue: any):
        self.__value = newValue

    def __str__(self):
        return f"Node with value {str(self.__value)}"

    def get(self) -> any:
        return self.__value

    def __eq__(self, other: 'Node'):
        return self.__hash__() == other.__hash__()

    def __gt__(self, other: 'Node'):
        return self.__value > other.get()

    def __gt__(self, other: 'Node'):
        return self.__value > other.get()

    def __hash__(self) -> int:
        return hash(f"{self.__create_date.timestamp}_{self.__value}")


class Linked_list():

    def __init__(self, primeValue: Node):
        self.head = primeValue
        self.tail = primeValue

    def add_first(self, new_node: Node):
        "Добавляем в начало списка"
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_node: Node):
        "Добавляем в конец списка"
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop_first(self) -> Node:
        "Выдёргиваем первый элемент"
        self.head = self.head.next
        tmp = self.head.prev
        self.head.prev = None
        return tmp

    def pop_last(self) -> Node:
        "Выдёргиваем последний элемент"
        self.tail = self.tail.prev
        tmp = self.tail.next
        self.tail.next = None
        return tmp

    def __str__(self) -> str:
        "строчное описание списка"
        out = ""
        node = self.head
        while node:
            out += f"{node}\n"
            node = node.next
        out.strip()
        return out

    def __len__(self):
        out = 0
        node = self.head
        while node:
            out += 1
            node = node.next
        return out

    def flip(self) -> None:
        """переворачиваем массив"""
        #  массив из одного значения не трогаем
        if len(self) == 1:
            return
        # из двух - не сложно
        # if len(self) == 2:
        #     temp = self.tail
        #     self.tail = self.head
        #     self.head = temp
        #     self.tail.prev = self.head
        #     self.tail.next = None
        #     self.head.next = self.tail
        #     self.head.prev = None
        #     return
        # ну поехали
        buffer = self.tail
        while buffer:
            copy_ = deepcopy(buffer)
            try:
                newL_list.add_last(copy_)
            except:
                newL_list = Linked_list(copy_)
            newL_list.tail.next = None
            buffer = buffer.prev
        self.head = newL_list.head
        self.tail = newL_list.tail
            

def main():
    # заполняем
    l_list = Linked_list(Node(1))
    l_list.add_first(Node(0))
    l_list.add_last(Node(2))
    l_list.add_last(Node(3))
    l_list.add_last(Node(4))
    l_list.add_last(Node(5))
    l_list.add_last(Node(6))
    l_list.add_last(Node(7))
    l_list.add_last(Node(8))
    # l_list.add_last(Node(9))

    # к теме не относится, просто тестирую на правах stack/queue
    l_list.add_first(Node("del"))
    l_list.pop_first()
    l_list.add_last(Node("del"))
    l_list.pop_last()

    # тестируем разворот
    print(f"primary:\n{l_list}")
    l_list.flip()
    print(f"after flip:\n{l_list}")


def check_hash_eq():
    """ для целей дз - вторично
    играюсь с хеш-функцией чтобы сравнивать head и tail если у нод
    одинаковые значения"""
    a = Node(1)
    b = Node(1)
    c = a
    print(f"ab:{a == b}")
    print(f"ac:{a == c}")


if __name__ == "__main__":
    main()
