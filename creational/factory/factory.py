from abc import ABC, abstractmethod


class Animal(ABC):
    
    @abstractmethod
    def sleep(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass


class Dog(Animal):

    def sleep(self) -> str:
        return "The DOG is sleeping!"
    
    def eat(self) -> str:
        return "The DOG is eating!"


class Penguin(Animal):

    def sleep(self) -> str:
        return "The PENGUIN is sleeping!"
    
    def eat(self) -> str:
        return "The PENGUIN is eating!"


class AnimalCreator(ABC):

    @abstractmethod
    def create_animal(self):
        pass

    def perform_animal_actions(self):
        animal = self.create_animal()
        print(animal.eat())
        print(animal.sleep())


class DogCreator(AnimalCreator):

    def create_animal(self) -> Dog:
        return Dog()


class PenguinCreator(AnimalCreator):

    def create_animal(self) -> Penguin:
        return Penguin()


def client_code(animal_creator: AnimalCreator):
    animal_creator.perform_animal_actions()


if __name__ == "__main__":
    print("Hello World!")

    print("\nCreating Dog!")
    client_code(DogCreator())

    print("\nCreating Penguin!")
    client_code(PenguinCreator())

