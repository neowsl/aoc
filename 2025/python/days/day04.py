def part1(data: str):
    grid = data.splitlines()
    N = len(grid)
    M = len(grid[0])

    row_dirs = [-1, -1, -1, 0, 0, 1, 1, 1]
    col_dirs = [-1, 0, 1, -1, 1, -1, 0, 1]

    ans = 0

    for i in range(N):
        for j in range(M):
            if grid[i][j] != "@":
                continue

            count = 0

            for k in range(len(row_dirs)):
                a = i + row_dirs[k]
                b = j + col_dirs[k]
                if 0 <= a < N and 0 <= b < M:
                    count += grid[a][b] == "@"

            if count < 4:
                ans += 1

    return ans


def part2(data: str):
    grid = [list(s) for s in data.splitlines()]
    N = len(grid)
    M = len(grid[0])

    row_dirs = [-1, -1, -1, 0, 0, 1, 1, 1]
    col_dirs = [-1, 0, 1, -1, 1, -1, 0, 1]

    ans = 0

    while True:
        mutated = False

        for i in range(N):
            for j in range(M):
                if grid[i][j] != "@":
                    continue

                count = 0

                for k in range(len(row_dirs)):
                    a = i + row_dirs[k]
                    b = j + col_dirs[k]
                    if 0 <= a < N and 0 <= b < M:
                        count += grid[a][b] == "@"

                if count < 4:
                    ans += 1
                    mutated = True
                    grid[i][j] = "."

        if not mutated:
            break

    return ans
