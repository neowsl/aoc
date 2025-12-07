def part1(data: str):
    head, tail = data.split("\n", 1)

    N = len(head)
    beams = [False] * N
    beams[head.find("S")] = True

    ans = 0

    for line in tail.splitlines():
        new_beams = beams
        for i, c in enumerate(line):
            if c == "." or not beams[i]:
                continue

            new_beams[i] = False
            ans += 1
            if i > 0:
                new_beams[i - 1] = True
            if i < N - 1:
                new_beams[i + 1] = True

        beams = new_beams

    return ans


def part2(data: str):
    head, tail = data.split("\n", 1)

    N = len(head)
    beams = [0] * N
    beams[head.find("S")] = 1

    for line in tail.splitlines():
        new_beams = beams.copy()
        for i, c in enumerate(line):
            if c == "." or not beams[i]:
                continue

            new_beams[i] = 0
            if i > 0:
                new_beams[i - 1] += beams[i]
            if i < N - 1:
                new_beams[i + 1] += beams[i]

        beams = new_beams

    return sum(new_beams)
