import pygame

SIZE = 8

def create_map():
    map = []
    for i in range(SIZE):
        row = [SIZE - i, "|"]

        for j in range(SIZE):

            if ( i + j ) % 2 == 0:
                row.append("[ ]")

            else:
                row.append("[ ]")


        map.append(row)

    return map




def print_map(mat):

    print("     A   B   C   D   E   F   G   H")
    print("   ---------------------------------")

    for row in mat:
        for col in row:
            print(col, end=" ")
        print("|")

    print("   ---------------------------------")

def player_turn(turn):
    if turn % 2 == 0:
        return "white"
    return "black"


def check_win():
    pass

def move_king(start_row, start_col ,end_row, end_col , turn ):
    pass

def move_queen():
    pass

def move_pawns():
    pass

def move_knight():
    pass

def move_rooks():
    pass

def move_bishops():
    pass

def main():
    mat = create_map()
    print_map(mat)

    

main()
