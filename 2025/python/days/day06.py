def part2(data: str):
    head, tail = data.split("*", 1)
    tail = "*" + tail
    tail = tail.strip()

    nums = head.splitlines()

    ans = 0

    for i, op in enumerate(tail):
        if op == " ":
            continue

        res = 0 if op == "+" else 1
        j = i
        while True:
            num = 0
            for row in head.splitlines():
                if j >= len(row) or row[j] == " ":
                    continue

                num *= 10
                num += ord(row[j]) - ord("0")

            if num == 0:
                break

            if op == "+":
                res += num
            else:
                res *= num

            j += 1

        ans += res

    return ans
