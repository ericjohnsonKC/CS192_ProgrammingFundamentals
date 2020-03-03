import random

class Mole:
    def __init__(self):
        self.coordinates = {'row':'', 'col':''}

    def initializePosition(self):
        mole.coordinates = {'row': random.randint(0, 3), 'col': random.randint(0, 3)}
        return mole.coordinates

    def move(self):
        newRow = self.coordinates['row'] + random.randint(-1, 1)
        while newRow < 0 or newRow > 3:
            newRow = self.coordinates['row'] + random.randint(-1, 1)
        newCol = self.coordinates['col'] + random.randint(-1, 1)
        while newCol < 0 or newCol > 3:
            newCol = self.coordinates['col'] + random.randint(-1, 1)
        self.coordinates = {'row': newRow, 'col': newCol}
        return self

class Player:
    def __init__(self):
        self.swingCount = 0
        self.swingCoordinates = {'row': '', 'col': ''}

    def swing(self):
        coordinate = input('Enter coordinates of the hole you want to swing at...> ')
        self.swingCoordinates = {'row': coordinate[0], 'col': coordinate[1]}
        return self


player = Player()
player.swing()
print(player.swingCoordinates)

# set mole initial position
# display grid
# get playerClubCoords
# increment swing counter
# move mole
# display grid
# while no collision
#   display grid
#   get playerClubCoords
#   increment swing counter
#   Move mole
#

