
def cost(x):
    c = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if abs(x[i] - x[j]) == abs(i - j):
                c += 1
    return c


def hill_climbing():
    x = [3, 1, 2, 0]

    while True:
        current_cost = cost(x)

        print("\nCurrent State:", x)
        print("Current Cost:", current_cost)

        if current_cost == 0:
            print("Goal State Reached!")
            break

        neighbors = []

        for i in range(4):
            for j in range(i + 1, 4):
                temp = x.copy()
                temp[i], temp[j] = temp[j], temp[i]

                neighbors.append((cost(temp), i, j, temp))

                print("Swap:", (i, j),
                      "Neighbor:", temp,
                      "Cost:", cost(temp))

        neighbors.sort(key=lambda a: (a[0], a[1], a[2]))

        best_cost, i, j, best = neighbors[0]

        print("Selected Swap:", (i, j))

        if best_cost >= current_cost:
            print("No better neighbor found!")
            break

        x = best

    print("\nFinal Solution:", x)
    print("Final Cost:", cost(x))

    print("\nChess Board:")
    for row in range(4):
        for col in range(4):
            print("Q" if x[col] == row else ".", end=" ")
        print()


hill_climbing()
