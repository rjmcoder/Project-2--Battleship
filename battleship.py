import sys
from players import Players

SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]


BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'

board = (['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'])

noOfPLayers = 2


def clear_screen():
    print("\033c", end="")


def print_board_heading():
    print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))


def print_board(board):
    print_board_heading()

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1


def initialize_the_game(board, i):
    print("Hi there, Welcome to the Battleship game")
    print("Let's start with your name")
    name = input(">: ")
    if i == 1:
        player1 = Players(name, board)
    if i == 2:
        player2 = Players(name, board)
    print("You will have to place 5 ships at different locations")
    ship_count = 0
    while ship_count < 5:
        ship_name = input("""Please select a ship from the following options to be placed on the Battle field.
    [A]ircraft Carrier, [B]attleship, [S]ubmarine, [C]ruiser, [P]atrol Boat or [Q] to quit: """).lower()
        if ship_name == 'q':
            sys.exit()
        if ship_name not in ['a', 'b', 's', 'c', 'p', 'q']:
            clear_screen()
            print("You selected an incorrect ship type, it has to be one of [A]ircraft Carrier, [B]attleship, [S]ubmarine, [C]ruiser, [P]atrol Boat")
            continue
        else:
            for n in SHIP_INFO:
                if n[0][0].lower() == ship_name:
                    name_of_ship = n[0]
                    spaces = n[1]

        loc = input("Where would you like to place the {} on the board ({} spaces) (eg., a2): ".format(name_of_ship, spaces))
        if loc == 'q':
            sys.exit()
        while True:
            try:
                x = int(''.join(list(loc)[1:]))
                y = list(loc)[0].lower()
                if ((x not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) or (y not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])):
                    clear_screen()
                    print("You need to be within Row = 10 and Column = J")
                    loc = input("Where would you like to place the {} on the board ({} spaces) (eg., a2): ".format(name_of_ship, spaces))
                    continue
                break
            except:
                clear_screen()
                print("You need to provide input in a2, b6, etc format")
                loc = input("Where would you like to place the {} on the board ({} spaces) (eg., a2): ".format(name_of_ship, spaces))
                continue
        location = (x, y)
        orient = input("""How would you like to place the {}?
    [H]orizontal, [V]ertical: """.format(name_of_ship)).lower()
        if orient == 'q':
            sys.exit()
        while orient not in ['h', 'v']:
            clear_screen()
            print("You selected an incorrect orientation, it has to be either [H]orizontal or [V]ertical")
            orient = input("""How would you like to place the {}?
      [H]orizontal, [V]ertical: """.format(name_of_ship)).lower()
            continue
        if i == 1:
            player1_add_ship = player1.add_ships(ship_name, location, orient)
            if player1_add_ship == 1:
                clear_screen()
                print_board(player1.playerBoard)
                ship_count += 1
            elif player1_add_ship == -1:
                print("You already have a ship at that location")
                continue
            elif player1_add_ship == -2:
                print("You need to be within Row = 10 and Column = J")
                continue
        if i == 2:
            player2_add_ship = player2.add_ships(ship_name, location, orient)
            if player2_add_ship == 1:
                clear_screen()
                print_board(player2.playerBoard)
                ship_count += 1
            elif player2_add_ship == -1:
                print("You already have a ship at that location")
                continue
            elif player2_add_ship == -2:
                print("You need to be within Row = 10 and Column = J")
                continue
    if i == 1:
        input("Press enter to continue..")
        clear_screen()
        return player1
    if i == 2:
        input("Press enter to continue..")
        clear_screen()
        return player2


def play_the_game(player, opponent):
    print("Its {}'s turn".format(player.name))
    input("Press enter to continue...")
    clear_screen()
    print("Your board:")
    print_board(player.playerBoard)
    print("")
    print("Opponents board with your moves:")
    print_board(opponent.playingBoard)
    print("")
    move = input("What location you want to place your move?: ")
    if move == 'q':
        sys.exit()
    while True:
        try:
            x = int(''.join(list(move)[1:]))
            y = list(move)[0].lower()
            if ((x not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) or (y not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])):
                clear_screen()
                print("You need to be within Row = 10 and Column = J")
                move = input("What location you want to place your move?: ")
                if move == 'q':
                    sys.exit()
                continue
            break
        except:
            clear_screen()
            print("You need to provide input in a2, b6, etc format")
            move = input("What location you want to place your move?: ")
            if move == 'q':
                sys.exit()
            continue
    move = (x, y)
    check_the_move = opponent.check_the_move(move)
    while check_the_move == -1:
        move = input("What location you want to place your move?: ")
        if move == 'q':
            sys.exit()
        while True:
            try:
                x = int(''.join(list(move)[1:]))
                y = list(move)[0].lower()
                if ((x not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) or (y not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])):
                    clear_screen()
                    print("You need to be within Row = 10 and Column = J")
                    move = input("What location you want to place your move?: ")
                    if move == 'q':
                        sys.exit()
                    continue
                break
            except:
                clear_screen()
                print("You need to provide input in a2, b6, etc format")
                move = input("What location you want to place your move?: ")
                if move == 'q':
                    sys.exit()
                continue
        move = (x, y)
        check_the_move = opponent.check_the_move(move)
    if check_the_move == 1:
        return player
    return 0


def main():
    player1 = initialize_the_game(board, 1)
    clear_screen()
    player2 = initialize_the_game(board, 2)
    player = player1
    opponent = player2
    winner = play_the_game(player, opponent)
    while winner == 0:
        player, opponent = opponent, player
        winner = play_the_game(player, opponent)
    input("Press enter to continue...")
    clear_screen()
    print("You win {}".format(winner.name))
    print("{}'s board".format(player1.name))
    print_board(player1.orgPlayerBoard)
    print("")
    print("{}'s board".format(player2.name))
    print_board(player2.orgPlayerBoard)
main()

