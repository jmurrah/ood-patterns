from datetime import datetime


class Singleton:

    _instance = None

    def __init__(self):
        self.created_at = str(datetime.now())

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance


if __name__ == "__main__":
    print("\nCreating singleton object!")
    obj1 = Singleton.get_instance()
    print(obj1.created_at)

    print("\nGetting instance again!")
    obj2 = Singleton.get_instance()
    print(obj2.created_at)
    