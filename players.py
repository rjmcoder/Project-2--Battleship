from ships import Patrol_boat
from ships import Cruiser
from ships import Submarine
from ships import Battleship
from ships import Aircraft_Carrier
from copy import deepcopy
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
ship_names_dict = {
    'a': 'Aircraft Carrier',
    'b': 'Battleship',
    'c': 'Cruiser',
    's': 'Submarine',
    'p': 'Patrol Boat'
}


def clear_screen():
    print("\033c", end="")


class Players(object):

    def __init__(self, name, board):
        self.name = name
        self.playerBoard = deepcopy(board)
        self.playingBoard = deepcopy(board)
        self.ships = []
        self.orgShips = []
        self.guessed = []

    def add_ships(self, ship_name, ship_loc, ship_orient):
        self.ship_name = ship_name
        self.ship_loc = ship_loc
        self.orient = ship_orient

        if self.ship_name == 'p':
            pb = Patrol_boat(self.ship_loc, self.orient)
            ship_coordinates = pb.place_the_ship()

        elif self.ship_name == 'c':
            cr = Cruiser(self.ship_loc, self.orient)
            ship_coordinates = cr.place_the_ship()

        elif self.ship_name == 's':
            sb = Submarine(self.ship_loc, self.orient)
            ship_coordinates = sb.place_the_ship()

        elif self.ship_name == 'b':
            bs = Battleship(self.ship_loc, self.orient)
            ship_coordinates = bs.place_the_ship()

        elif self.ship_name == 'a':
            ac = Aircraft_Carrier(self.ship_loc, self.orient)
            ship_coordinates = ac.place_the_ship()

        for i in ship_coordinates:  # check if any of the locations is already taken
            for j in self.ships:
                for k in j[1]:
                    if i == k:
                        return -1
            if i[0] > 9 or i[1] > 9:
                return -2
        for i in ship_coordinates:      # place the ship on the board
            if self.orient == 'h':
                self.playerBoard[i[0]][i[1]] = '-'
            elif self.orient == 'v':
                self.playerBoard[i[0]][i[1]] = '|'
        self.ships.append([self.ship_name, ship_coordinates])
        self.orgPlayerBoard = deepcopy(self.playerBoard)
        self.orgShips = deepcopy(self.ships)
        return 1

    def check_the_move(self, move):
        x = move[0] - 1
        y = cols.index(move[1])
        hit = False
        sunk = False
        if (x, y) in self.guessed:
            print("You have already guessed that location...try again")
            return -1
        else:
            self.guessed.append((x, y))
        for i in self.ships:
            for j in i[1]:
                if (x, y) == j:
                    self.playingBoard[x][y] = '*'
                    self.playerBoard[x][y] = '*'
                    hit = True
                    clear_screen()
                    print("You hit {}'s ship".format(self.name))
                    break
            if hit is True:
                i[1].remove(j)
                if len(i[1]) == 0:
                    sunk = True
                    clear_screen()
                    print("You sunk {}'s {}".format(self.name, ship_names_dict[i[0]]))
            if hit is True:
                break
        else:
            self.playingBoard[x][y] = '.'
            self.playerBoard[x][y] = '.'
            clear_screen()
            print("You missed")
            return 0
        if sunk is True:
            self.ships.remove(i)
            for i in self.orgShips:
                if (x, y) in i[1]:
                    for k in i[1]:
                        self.playingBoard[k[0]][k[1]] = '#'
                        self.playerBoard[k[0]][k[1]] = '#'
        if len(self.ships) == 0:
            return 1

