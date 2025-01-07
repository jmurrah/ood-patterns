class SquareHose:

    shape = "SQUARE"

    def attach_hose(self):
        print("Attaching SQUARE HOSE!")


# The Adaptee (Useful functionality we need)
class RoundFaucet:

    def attach_round_hose(self):
        print("Attaching the round hose!")


# The Adapter (Converting square to round)
class HoseAdapter(SquareHose, RoundFaucet):

    def attach_hose(self):
        print("Doing some conversion magic!")
        self.attach_round_hose()


if __name__ == "__main__":
    square_hose = HoseAdapter()
    square_hose.attach_hose()
