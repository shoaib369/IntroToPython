__author__ = 'moshoaib'


def print_grid(gridSize):
    for i in range(gridSize):
        if i % 5 == 0:
            for j in range(gridSize):
                if j % 5 == 0:
                    print('+', end="")
                else:
                    print('-', end="")
        else:
            for j in range(gridSize):
                if j % 5 == 0:
                    print('|', end="")
                else:
                    print(' ', end="")
        print("")

print_grid(16)