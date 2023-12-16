size=int(input())

def print_pseudo_chessboard(size):
    for i in range(size, 0, -1):
        for j in range(1, size + 1):
            print(f'{chr(64 + j)}{i}', end=' ')
        print()

print_pseudo_chessboard(size)
