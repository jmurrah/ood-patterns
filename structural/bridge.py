# The IMPLEMENTATION class (the backend code)
class Device:

    def power_on(self):
        print("Device is powered ON!")
    
    def power_off(self):
        print("Device is powered OFF!")


# The ADAPTER class (what the user interacts with)
class Remote:

    def __init__(self, device: Device):
        self.device = device
    
    def turn_on_device(self):
        print("Using remote to turn ON device!")
        self.device.power_on()
    
    def turn_off_device(self):
        print("Using remote to turn OFF device!")
        self.device.power_off()


if __name__ == "__main__":
    remote = Remote(device=Device())
    remote.turn_on_device()
    remote.turn_off_device()