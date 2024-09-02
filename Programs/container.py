# container.py
from abc import ABC, abstractmethod

class ContainerProtocol(ABC):
    @abstractmethod
    def insert(self, item):
        ...

    @abstractmethod
    def insert_all(self, items):
        ...

    @abstractmethod
    def display(self):
        ...

class Container(ContainerProtocol):
    def __init__(self):
        self._items = [ ]

    def insert(self, item):
        self._items.append(item)

    def insert_all(self, items):
        for item in items:
            self.insert(item)

    def display(self):
        for item in self._items:
            print(item)

## some bug
#class ContainerCount(Container):
#    def __init__(self):
#        self._count = 0
#        super().__init__()
#
#    def insert(self, item):
#        self._count = self._count + 1
#        super().insert(item)
#
#    def insert_all(self, items):
#        self._count = self._count + len(items)
#        super().insert_all(items)
#
#    def count(self):
#        return self._count

# Composition (HAS-A)
# this is composite class
class ContainerCount:
    def __init__(self, container):
        self._count = 0
        self.container = container      # <----- Container object (dependancy injection)

    def insert(self, item):
        self.container.insert(item)     # delegating        # demo.insert()
        self._count = self._count + 1

    def insert_all(self, items):
        self.container.insert_all(items)        # delegating
        self._count = self._count + len(items)

    def display(self):
        self.container.display()    # delegating

    def count(self):
        return self._count


class Demo:
    def greet(self):
        return "hello world"

    def insert(self, item):
        print("Inserting...")

    def insert_all(self, items):
        print("Inserting all....")

class NumericContainer(Container):
    def insert(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError("Only Numbers are allowed")
        super().insert(item)


# container = NumericContainer()
demo = Demo()
# we are passing container objec or object instance of Container class
# to ContainerCount class
container_count = ContainerCount(demo)