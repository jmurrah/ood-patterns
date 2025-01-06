from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass
    
    @abstractmethod
    def step_three(self):
        pass
    
    @abstractmethod
    def step_four(self):
        pass

    @abstractmethod
    def get_product(self):
        pass


class ProductABuilder(Builder):
    
    def reset(self):
        self.steps = []

    def step_one(self):
        self.steps.append("1A")

    def step_two(self):
        self.steps.append("2A")

    def step_three(self):
        self.steps.append("3A")

    def step_four(self):
        self.steps.append("4A")
    
    def get_product(self) -> list[str]:
        return self.steps
    

class ProductBBuilder(Builder):

    def reset(self):
        self.steps = []

    def step_one(self):
        self.steps.append("1B")

    def step_two(self):
        self.steps.append("2B")

    def step_three(self):
        self.steps.append("3B")

    def step_four(self):
        self.steps.append("4B")
    
    def get_product(self) -> list[str]:
        return self.steps


class Director(ABC):

    def make_reverse_combo(self, builder: Builder):
        print("Making reverse combo!")
        builder.reset()
        builder.step_four()
        builder.step_three()
        builder.step_two()
        builder.step_one()
        print(builder.get_product())

    def make_anagram_combo(self, builder: Builder):
        print("Making anagram combo!")
        builder.reset()
        builder.step_four()
        builder.step_two()
        builder.step_two()
        builder.step_four()
        print(builder.get_product())


def client_code(builder: Builder):
    director = Director()
    director.make_reverse_combo(builder)
    director.make_anagram_combo(builder)


if __name__ == "__main__":
    print("Hello World!")

    print("\nUsing Builder A!")
    client_code(ProductABuilder())

    print("\nUsing Builder B!")
    client_code(ProductBBuilder())