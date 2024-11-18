#grid file
import random
import os
import string
import time
import sys
import copy

#generate grid method

#generate hidden grid

#temp display method

class Grid:
    def __init__(self,size):
        self.size = size
        self.grid = []
        self.score = 0
        self.guesses = 0
        self.min_guesses = 0

    def generateGrid(self):
        # this produces a list with all the elements that will exist in the grid.
        pairs = [i for i in range(0, (self.size * self.size // 2)) for _ in range(2)]
        # this shuffles the elements
        random.shuffle(pairs)
        self.grid = [pairs[i:i + self.size] for i in range(0, len(pairs), self.size)]


    def __str__(self):
        return f"This grid's dimensions are {self.size}x{self.size}"

    def hidden_grid(self):

        self.grid =[["X" for _ in range(self.size)] for _ in range(self.size)]

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.grid == other.grid


    def display_grid(self):
        os.system('cls')
        letters = string.ascii_uppercase
        print("--------------------------")
        print("|       Brain Buster     |")
        print("--------------------------")
        x = 0
        print("   ", end=" ")
        for i in range(self.size):
            print(f"[{letters[i]}]", end=" ")
            if i == self.size - 1:
                print()
        for row in self.grid:
            print(f"[{x}]  ", end="")
            print("   ".join(str(val) for val in row))
            x += 1

    def option1_correct(self, value, index1, index2):
        self.grid[index1[1]][index1[0]] = self.grid[index2[1]][index2[0]] = value
        self.display_grid()

    def option1_wrong(self, main_grid, index1, index2):
        temp1 = self.grid[index1[1]][index1[0]]
        temp2 = self.grid[index2[1]][index2[0]]

        self.grid[index1[1]][index1[0]] = main_grid.grid[index1[1]][index1[0]]
        self.grid[index2[1]][index2[0]] = main_grid.grid[index2[1]][index2[0]]
        self.display_grid()
        time.sleep(2)

        self.grid[index1[1]][index1[0]] = temp1
        self.grid[index2[1]][index2[0]] = temp2
        self.display_grid()

    def option2(self, main_grid):
        letters = string.ascii_uppercase
        input1 = input("Enter cell coordinates (e.g., a0): ")
        index1=[0,0]
        index2=[0,0]

        for i in range(len(letters) - 1):
            if input1[0].upper() == letters[i]:
                index1[0] = i
                index1[1] = int(input1[1])
        temp = self.grid[index1[1]][index1[0]] = main_grid.grid[index1[1]][index1[0]]

        for i in range(self.size):
            for j in range(self.size):
                if  temp == main_grid.grid[j][i] and index1[0]!=i and index1[1] != j:
                    index2 = [i,j]

            self.grid[index2[1]][index2[0]] = main_grid.grid[index2[1]][index2[0]]
            self.display_grid()

    def option3(self, main_grid):
        self.display_grid()
        self.grid = copy.deepcopy(main_grid.grid)
        self.display_grid()


    def option5(self):
        print("Thank you for playing!")
        print("Goodbye!")
        sys.exit(0)

    def calc_score(self):
        self.score = (self.min_guesses / self.guesses) * 100
        # print(f"\nOh Happy Day. You've won!! Your score is : {self.score:.1f}")


    # def option1_wrong(self,index1, index2):

    #
    # def option1_wrong(self):



            # if grid.grid[index1[1]][index1[0]] != grid.grid[index2[1]][index2[0]]:




        # print(self.grid[index1[1]][index1[0]])
        # print(self.grid[index2[1]][index2[0]])

        # if self.grid[index1[0]][index1[1]] != "X":