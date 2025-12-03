def part2(data: str):
    ans = 0

    for line in data.splitlines():
        k = 12
        rem = len(line) - k
        s: list[str] = []

        for c in line:
            while s and rem > 0 and s[-1] < c:
                s.pop()
                rem -= 1

            s.append(c)

        s = s[:k]
        ans += int("".join(s))

    return ans
