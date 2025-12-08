import heapq


def dist_sq(p1, p2):
    return [(x1 - x2) ** 2 for x1, x2 in zip(p1, p2)]


def part1(data: str):
    pq = []
    points: list[list[int]] = []

    for line in data.splitlines():
        point = line.split(",")
        point = [int(s) for s in point]

        for other in points:
            heapq.heappush(pq, (dist_sq(point, other), point, other))

        points.append(point)

    parent = {}
