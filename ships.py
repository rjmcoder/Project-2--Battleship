cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


class Patrol_boat:
    length = 2

    def __init__(self, begin, orient):
        self.begin = begin
        self.orient = orient

    def place_the_ship(self):
        x = self.begin[0] - 1
        y = cols.index(self.begin[1])
        ship_coord = []
        if self.orient == 'h':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                y += 1
        if self.orient == 'v':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                x += 1
        return ship_coord


class Cruiser:
    length = 3

    def __init__(self, begin, orient):
        self.begin = begin
        self.orient = orient

    def place_the_ship(self):
        x = self.begin[0] - 1
        y = cols.index(self.begin[1])
        ship_coord = []
        if self.orient == 'h':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                y += 1
        if self.orient == 'v':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                x += 1
        return ship_coord


class Submarine:
    length = 3

    def __init__(self, begin, orient):
        self.begin = begin
        self.orient = orient

    def place_the_ship(self):
        x = self.begin[0] - 1
        y = cols.index(self.begin[1])
        ship_coord = []
        if self.orient == 'h':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                y += 1
        if self.orient == 'v':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                x += 1
        return ship_coord


class Battleship:
    length = 4

    def __init__(self, begin, orient):
        self.begin = begin
        self.orient = orient

    def place_the_ship(self):
        x = self.begin[0] - 1
        y = cols.index(self.begin[1])
        ship_coord = []
        if self.orient == 'h':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                y += 1
        if self.orient == 'v':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                x += 1
        return ship_coord


class Aircraft_Carrier:
    length = 5

    def __init__(self, begin, orient):
        self.begin = begin
        self.orient = orient

    def place_the_ship(self):
        x = self.begin[0] - 1
        y = cols.index(self.begin[1])
        ship_coord = []
        if self.orient == 'h':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                y += 1
        if self.orient == 'v':
            for i in range(0, self.length):
                ship_coord.append((x, y))
                x += 1
        return ship_coord

