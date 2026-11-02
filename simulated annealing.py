
import random
import math

N = 8

def cost(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def simulated_annealing():
    board = [random.randint(0, N - 1) for _ in range(N)]

    T = 100
    cooling_rate = 0.99

    while T > 0.01:
        current_cost = cost(board)

        if current_cost == 0:
            return board

        new_board = board.copy()

        col = random.randint(0, N - 1)
        row = random.randint(0, N - 1)

        new_board[col] = row

        new_cost = cost(new_board)
        delta = new_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / T):
            board = new_board

        T = T * cooling_rate

    return board


solution = simulated_annealing()

print("Final Solution:", solution)
print("Cost:", cost(solution))

print("\nChess Board:")
for row in range(N):
    for col in range(N):
        if solution[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
