def game_of_life(board):
    m = len(board)
    n = len(board[0])

    # Directions for all 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    new_board = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):

            live_neighbors = 0

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n:
                    live_neighbors += board[ni][nj]

            # Live cell
            if board[i][j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0

            # Dead cell
            else:
                if live_neighbors == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0

    return new_board


# Test Case 1
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

result = game_of_life(board)

for row in result:
    print(row)


print()


# Test Case 2
board = [
    [1, 1],
    [1, 0]
]

result = game_of_life(board)

for row in result:
    print(row)