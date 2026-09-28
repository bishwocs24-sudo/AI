# 8-Puzzle using DFS and BFS

from collections import deque

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]


# Generate possible moves
def moves(state):
    result = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    directions = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in directions:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_state = state.copy()
            new_zero = r * 3 + c

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            result.append((new_state, move))

    return result


# DFS
def dfs(start):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        for new_state, move in moves(state):
            if tuple(new_state) not in visited:
                stack.append((new_state, path + [move]))

    return None


# BFS
def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        for new_state, move in moves(state):
            if tuple(new_state) not in visited:
                queue.append((new_state, path + [move]))

    return None


# Initial state
start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

print("Initial State:")
for i in range(0, 9, 3):
    print(start[i:i+3])


# DFS
dfs_solution = dfs(start)
print("\nDFS Solution:", dfs_solution)
print("DFS Number of moves:", len(dfs_solution))


# BFS
bfs_solution = bfs(start)
print("\nBFS Solution:", bfs_solution)
print("BFS Number of moves:", len(bfs_solution))
