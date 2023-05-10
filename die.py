# Die class

import random

class Die():
    """The die class will be used to create die objects
    the die will have x sides where x is the number it is created with"""
    def __init__(self, sides):
        self.sides = sides
        self.facevalue = 0

    def roll(self):
        """roll the die,
        return a random number between 1 and the number of sides"""
        self.facevalue = random.randint(1, self.sides)
        return self.facevalue

    def __repr__(self):
        return f'D{self.sides} rolled: {str(self.facevalue)}'

# d20 = Die(20)

# for i in range(30):
#     d20.roll()
#     print(repr(d20))
