keymap = {
    1: "[]",
    2: "[]",
    3: "[]",
    4: "[]",
    5: "[]",
    6: "[]",
    7: "[]",
    8: "[]",
    9: "[]"
}


def print_board():

    print(f"{keymap[1]}{keymap[2]}{keymap[3]}")
    print(f"{keymap[4]}{keymap[5]}{keymap[6]}")
    print(f"{keymap[7]}{keymap[8]}{keymap[9]}")


def check_win(current_player):
    if current_player in keymap[1] and current_player in keymap[2] and current_player in keymap[3]:
        return True
    elif current_player in keymap[1] and current_player in keymap[4] and current_player in keymap[7]:
        return True
    elif current_player in keymap[1] and current_player in keymap[5] and current_player in keymap[9]:
        return True
    elif current_player in keymap[2] and current_player in keymap[5] and current_player in keymap[8]:
        return True
    elif current_player in keymap[3] and current_player in keymap[5] and current_player in keymap[7]:
        return True
    elif current_player in keymap[3] and current_player in keymap[6] and current_player in keymap[9]:
        return True
    elif current_player in keymap[4] and current_player in keymap[5] and current_player in keymap[6]:
        return True
    elif current_player in keymap[7] and current_player in keymap[8] and current_player in keymap[9]:
        return True
    else:
        return False


current_player = "X"


def take_input(current_player):
    selection = ""
    while selection != "10":
        selection = input(
            f"Hi player {current_player}: please select a square from 1 - 9 ")

        keymap[int(selection)] = f"[{current_player}]"
        print_board()
        is_winner = check_win(current_player)
        if is_winner:
            print(f"{current_player} wins!")
            break

        if all(len(value) == 3 for value in keymap.values()):
            print("It's a tie!")
            break
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


take_input(current_player)
