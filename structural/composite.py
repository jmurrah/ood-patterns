from abc import ABC, abstractmethod


class CommonInterface(ABC):

    @abstractmethod
    def search(self, count: int):
        pass


class Leaf(CommonInterface):

    def search(self, count: int):
        print("Made it to a leaf!!!")
    

class ComplexClass(CommonInterface):

    def __init__(self, children: list[CommonInterface]):
        self.children = children

    def search(self, count: int):
        print("LVL: " + str(count) + "\tStill searching...")
        for child in self.children:
            child.search(count + 1)


def client_code(object: CommonInterface):
    object.search(0)


if __name__ == "__main__":
    leaves1 = [Leaf() for _ in range(5)]
    leaves2 = [Leaf() for _ in range(10)]
    c1 = ComplexClass(leaves1)
    c2 = ComplexClass(leaves2)
    c1.children.append(c2)

    client_code(c1)

