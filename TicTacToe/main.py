def display_table(list_of_moves):

    for index in range(len(list_of_moves)):

        if list_of_moves[index] is None:
            print(" ", end="")
        else:
            print(list_of_moves[index], end="")

        if index+1 == len(list_of_moves):
            print("\n")
        elif (index + 1) % 3 == 0:
            print("\n-+-+-")
        else:
            print("|", end="")


def player_move(player):

    print("It's your turn, " + player + "\nWhere do you want to put your " + turn + "?")
    print("Line Column")
    x, y = input().split()
    x = int(x)
    y = int(y)
    if move_table[(x - 1) * 3 + (y - 1)] is None:
        move_table[(x - 1) * 3 + (y - 1)] = turn
    else:
        print('Please enter a correct line and column.')
        player_move(player)


def verify_won():
    if move_table[0] == move_table[1] == move_table[2] is not None:
        return True
    elif move_table[3] == move_table[4] == move_table[5] is not None:
        return True
    elif move_table[6] == move_table[7] == move_table[8] is not None:
        return True
    elif move_table[0] == move_table[3] == move_table[6] is not None:
        return True
    elif move_table[1] == move_table[4] == move_table[7] is not None:
        return True
    elif move_table[2] == move_table[5] == move_table[8] is not None:
        return True
    elif move_table[0] == move_table[4] == move_table[8] is not None:
        return True
    elif move_table[6] == move_table[4] == move_table[2] is not None:
        return True
    return False


if __name__ == '__main__':
    turn = 'X'
    move_table = [None] * 9

    print("Welcome my Friends to our TicTac Toe!\n"
          "Firstly you need to set your names\n"
          "After that you need to write the line and column"
          "where do you want to put you X/O.\n"
          )

    print("Text the name of first player")
    first_player = input()
    while len(first_player) == 0:
        print("Please enter the name of first player")
        first_player = input()

    print("Enter the name of the second player")
    second_player = input()
    while len(second_player) == 0:
        print("Please enter the name of second player")
        second_player = input()

    for i in range(9):

        display_table(move_table)
        if turn == 'X':
            player_move(first_player)
        else:
            player_move(second_player)

        if verify_won():
            print("Game Over!")
            print("The winner is", end=" ")
            if turn == 'X':
                print(first_player)
            else:
                print(second_player)
            exit()

        if turn == 'X':
            turn = 'Y'
        else:
            turn = 'X'

    print("It's a Tie.")
