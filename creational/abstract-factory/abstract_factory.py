from abc import ABC, abstractmethod


class Table(ABC):
    
    @abstractmethod
    def set_table(self):
        pass


class Chair(ABC):
    
    @abstractmethod
    def sit_down(self):
        pass


class Bed(ABC):

    @abstractmethod
    def lay_down(self):
        pass


class VictorianTable(Table):
    
    def set_table(self) -> str:
        return "Setting my VICTORIAN table!"


class VictorianChair(Chair):
    
    def sit_down(self) -> str:
        return "Sitting down in my VICTORIAN chair!"


class VictorianBed(Bed):

    def lay_down(self) -> str:
        return "Laying down in my VICTORIAN bed!"
    

class ModernTable(Table):
    
    def set_table(self) -> str:
        return "Setting my MODERN table!"


class ModernChair(Chair):
    
    def sit_down(self) -> str:
        return "Sitting down in my MODERN chair!"


class ModernBed(Bed):

    def lay_down(self) -> str:
        return "Laying down in my MODERN bed!"


class FurnitureFactory(ABC):
    
    @abstractmethod
    def create_table(self) -> Table:
        pass

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_bed(self) -> Bed:
        pass

    def use_furniture(self):
        table = self.create_table()
        chair = self.create_chair()
        bed = self.create_bed()
        print(table.set_table())
        print(chair.sit_down())
        print(bed.lay_down())



class VictorianFurnitureFactory(FurnitureFactory):

    def create_table(self) -> VictorianTable:
        return VictorianTable()

    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_bed(self) -> VictorianBed:
        return VictorianBed()
    

class ModernFurnitureFactory(FurnitureFactory):

    def create_table(self) -> ModernTable:
        return ModernTable()

    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_bed(self) -> ModernBed:
        return ModernBed()
    

def client_code(furniture_factory: FurnitureFactory):
    furniture_factory.use_furniture()


if __name__ == "__main__":
    print("Hello World!")

    print("\nCreating Victorian Furniture in my Victorian Furniture Factory!")
    client_code(VictorianFurnitureFactory())

    print("\nCreating Modern Furniture in my Modern Furniture Factory!")
    client_code(ModernFurnitureFactory())