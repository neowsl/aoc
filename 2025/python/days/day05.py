def part1(data: str):
    ranges, ids = [d.splitlines() for d in data.split("\n\n")]
    ranges = [(int(a), int(b)) for r in ranges for a, b in [r.split("-")]]
    ids = map(int, ids)

    ans = 0

    for id in ids:
        fresh = False
        for r in ranges:
            if r[0] <= id <= r[1]:
                fresh = True

        ans += fresh

    return ans


def part2(data: str):
    ranges, _ = [d.splitlines() for d in data.split("\n\n")]
    ranges = [(int(a), int(b)) for r in ranges for a, b in [r.split("-")]]

    dp: list[tuple[int, int]] = []
    for r in ranges:
        new_dp: list[tuple[int, int]] = []
        new_range: tuple[int, int] | None = None

        for x in dp:
            old = x if new_range is None else new_range
            if x[0] <= r[0] <= x[1]:
                new_range = (x[0], max(old[1], r[1]))
            elif x[0] <= r[1] <= x[1]:
                new_range = (min(old[0], r[0]), x[1])
            elif x[0] < r[0] or x[1] > r[1]:
                new_dp.append(x)

        if new_range is None:
            new_dp.append(r)
        else:
            new_dp.append(new_range)

        dp = new_dp

    ans = 0
    for x in dp:
        ans += x[1] - x[0] + 1

    return ans
