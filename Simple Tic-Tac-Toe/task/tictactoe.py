cells_dict = {(1, 1): " ", (1, 2): " ", (1, 3): " ",
              (2, 1): " ", (2, 2): " ", (2, 3): " ",
              (3, 1): " ", (3, 2): " ", (3, 3): " "}

x = ["X", "X", "X"]
o = ["O", "O", "O"]

game = True
player = "player_1"


def print_grid():
    print("---------")
    print(f"| {cells_dict[(1, 1)]} {cells_dict[(1, 2)]} {cells_dict[(1, 3)]} |")
    print(f"| {cells_dict[(2, 1)]} {cells_dict[(2, 2)]} {cells_dict[(2, 3)]} |")
    print(f"| {cells_dict[(3, 1)]} {cells_dict[(3, 2)]} {cells_dict[(3, 3)]} |")
    print("---------")


def update_grid(new):
    global cells_dict
    global player

    if cells_dict[(new)] == " ":
        if player == "player_1":
            cells_dict[(new)] = "X"
        else:
            cells_dict[(new)] = "O"
        print_grid()
    else:
        print("This cell is occupied! Choose another one!")
        cord_validation()


def cord_validation():
    cells = input("Enter the coordinates: ").split()

    if len(cells) == 2 and (cells[0].isdigit() and cells[1].isdigit()):
        if 0 < int(cells[0]) < 4 and 0 < int(cells[1]) < 4:
            new_list = []
            for item in cells:
                new_list.append(int(item))
            new = tuple(new_list)
            update_grid(new)
            return
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
    cord_validation()


def matches(list_grid):
    colums = []

    k = 0

    while k < 3:
        i = k
        while i < len(list_grid):
            colums.append(list_grid[i])
            i += 3
        k += 1

    i = 0

    while i < len(list_grid):
        colums.append(list_grid[i])
        i += 4

    i = 2

    while i < len(list_grid):
        colums.append(list_grid[i])
        i += 2
    return colums


def listing(my_input):
    new = []

    for i in range(0, len(my_input), 3):
        new.append(my_input[i:i + 3])
    return new


def validation():
    global game
    global player

    new_grid = cells_dict.values()
    list_grid = list(new_grid)

    final_row = (listing(matches(list_grid)) + listing(list_grid))
    for i in final_row:
        if i == x:
            print("X wins")
            exit()
        elif i == o:
            print("O wins")
            exit()
    if not any(" " in sl for sl in final_row):
        print("Draw")
        exit()

def main():
    global player

    print_grid()
    while True:
        cord_validation()
        validation()
        if player == "player_1":
          player = "player_2"
        elif player == "player_2":
          player = "player_1"

main()
