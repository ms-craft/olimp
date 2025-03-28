# Вторая задача
def cross_check(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(set(points))

    lower = []
    for p in points:
        while len(lower) >= 2 and cross_check(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_check(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def poligon_area(verticales):
    n = len(verticales)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += verticales[i][0] * verticales[j][1] - verticales[j][0] * verticales[i][1]

    return abs(area) / 2

def minimalize_area(points):
    hulls = convex_hull(points)

    return poligon_area(hulls)


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
print(minimalize_area(points))