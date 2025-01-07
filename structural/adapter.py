
class RoundHose:

    shape = "ROUND"

class SquareHose:

    shape = "SQUARE"


class SquareToRoundHoseAdapter:

    @classmethod
    def attach_hose(cls, square_hose: SquareHose):
        print("Initial Hose: " + square_hose.shape)
        print("Doing some conversion magic!")
        round_hose = RoundHose()
        print("Final Hose: " + round_hose.shape)
        RoundFaucet.attach_hose(round_hose)


class RoundFaucet:

    @classmethod
    def attach_hose(cls, round_hose: RoundHose):
        print("Attaching the round hose!")
        print(round_hose.shape)


if __name__ == "__main__":
    square_hose = SquareHose()
    SquareToRoundHoseAdapter.attach_hose(square_hose)
