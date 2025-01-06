from abc import ABC, abstractmethod
import copy


class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class PrototypeDog(Prototype):

    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color
    
    def clone(self):
        return copy.deepcopy(self)
    
    def bark(self):
        return "BARK says the " + str(self.age) + " year old " + self.color + " DOG named " + self.name + "!"
    

def client_code():
    print("\nCreating original Dog!")
    orig_dog = PrototypeDog(name="Max", age=11, color="Blue")
    print(orig_dog.bark())
    print("Memory address of the original dog: " + str(id(orig_dog)))

    print("\nCloning Dog!")
    cloned_dog = orig_dog.clone()
    print(cloned_dog.bark())
    print("Memory address of the cloned dog: " + str(id(cloned_dog)))


if __name__ == "__main__":
    print("Hello World!")
    client_code()