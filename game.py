import grid
import string
import os
import time
import sys
import copy

letters = string.ascii_uppercase

def menu():
    print("\n1. Let me select two elements")
    print("2. Uncover one element for me")
    print("3. I give up - reveal the grid")
    print("4. New Game")
    print("5. Exit")
def option1(grid, hidden_grid):
    input1 = input("Enter cell coordinates (e.g., a0): ")
    input2 = input("Enter cell coordinates (e.g., a0): ")
    index1 = [0, 0]
    index2 = [0, 0]

    for i in range(len(letters) - 1):
        if input1[0].upper() == letters[i]:
            index1[0] = i
            index1[1] = int(input1[1])
        if input2[0].upper() == letters[i]:
            index2[0] = i
            index2[1] = int(input2[1])

    if index1[0] >= hidden_grid.size or index1[1] >= hidden_grid.size or index2[0] >= hidden_grid.size or index2[1] >= hidden_grid.size:
            print("\ncoordinates out of bound.")
            return

    if grid.grid[index1[1]][index1[0]] == grid.grid[index2[1]][index2[0]]:
        value = grid.grid[index1[1]][index1[0]]
        hidden_grid.option1_correct(value, index1, index2)

    if grid.grid[index1[1]][index1[0]] != grid.grid[index2[1]][index2[0]]:
        hidden_grid.option1_wrong(grid, index1, index2)

    hidden_grid.guesses += 1


def main():
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("Please enter an integer")
        sys.exit(1)

    main_grid = grid.Grid(size)
    hidden_grid = grid.Grid(size)
    main_grid.generateGrid()
    hidden_grid.hidden_grid()

    if size == 2:
        hidden_grid.min_guesses = 2
    elif size == 4:
        hidden_grid.min_guesses = 8
    elif size == 6:
        hidden_grid.min_guesses = 18
    else:
        print("Invalid argument. Please enter 2, 4, or 6.")
        sys.exit(1)
    while True:
            while True:
                hidden_grid.display_grid()
                menu()
                x = int(input("\nSelect: "))

                if(x == 1):
                    option1(main_grid, hidden_grid)
                elif(x == 2):
                    hidden_grid.option2(main_grid)
                elif(x == 3):
                    hidden_grid.option3(main_grid)
                    hidden_grid.score = 0
                    break
                elif(x == 4):
                    main_grid.generateGrid()
                    hidden_grid.hidden_grid()
                    hidden_grid.score = 0
                    hidden_grid.guesses = 0
                elif(x == 5):
                    hidden_grid.option5()
                else:
                    print("\nInvalid input")

                if hidden_grid.grid == main_grid.grid:
                    break

            if hidden_grid.guesses == 0:
                hidden_grid.score = 0
            else:
                hidden_grid.calc_score()

            if hidden_grid.score == 0:
                print("\nYou cheated-Loser!. Your score is 0!")

            else:
                print("\nOh happy Day. You've won!! Your score is: ", hidden_grid.score)

            y = input("\nDo you want to play again? (y/n): ")

            if y == "n" or y == "N":
                print("Thank you for playing!")
                sys.exit(0)
            else:
                main_grid.generateGrid()
                hidden_grid.hidden_grid()
                hidden_grid.score = 0
                hidden_grid.guesses = 0




if __name__ == "__main__":
     main()