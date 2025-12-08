import heapq
import math

from scipy.cluster.hierarchy import DisjointSet


def dist_sq(p1: tuple[int, ...], p2: tuple[int, ...]):
    return sum([(x1 - x2) ** 2 for x1, x2 in zip(p1, p2)])


def part1(data: str):
    pq = []
    points: list[tuple[int, ...]] = []

    for line in data.splitlines():
        point = line.split(",")
        point = tuple([int(s) for s in point])

        for other in points:
            heapq.heappush(pq, (dist_sq(point, other), point, other))

        points.append(point)

    ds = DisjointSet(points)
    for i in range(min(1000, len(pq))):
        _, p1, p2 = heapq.heappop(pq)
        ds.merge(p1, p2)

    count: dict[tuple[int, ...], int] = {}
    for point in points:
        root = ds[point]
        if root not in count:
            count[root] = 0
        count[root] += 1

    pq2 = []
    for key in count:
        heapq.heappush(pq2, count[key])
        if len(pq2) > 3:
            heapq.heappop(pq2)

    return math.prod(pq2)


def part2(data: str):
    pq = []
    points: list[tuple[int, ...]] = []

    for line in data.splitlines():
        point = line.split(",")
        point = tuple([int(s) for s in point])

        for other in points:
            heapq.heappush(pq, (dist_sq(point, other), point, other))

        points.append(point)

    ds = DisjointSet(points)
    root = points[0]
    while True:
        _, p1, p2 = heapq.heappop(pq)
        ds.merge(p1, p2)

        if len(ds.subsets()) == 1:
            break

    return p1[0] * p2[0]
