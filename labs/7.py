from sympy import cos, sin


def fn(x):
    return 1.2 * x**2 - sin(10 * x)


def dif1(x):
    return 2.4 * x - 10 * cos(10 * x)


def dif2(x):
    return 2.4 + 10 * sin(10 * x) * 10


intervals = [
    (-0.6, -0.5),
    (-0.4, -0.3),
    (-0.1, 0.1),
    (0.25, 0.35),
    (0.65, 0.7),
    (0.8, 0.85),
]
eps = 1e-9

for i in range(len(intervals)):
    if dif2(intervals[i][0]) * fn(intervals[i][0]) > dif2(intervals[i][1]) * fn(
        intervals[i][1]
    ):
        kas0 = intervals[i][0]
        hor0 = intervals[i][1]
        while abs(hor0 - kas0) > eps:
            kas1 = kas0 - fn(kas0) / dif1(kas0)
            hor1 = hor0 - fn(hor0) * (kas0 - hor0) / (fn(kas0) - fn(hor0))
            kas0 = kas1
            hor0 = hor1
            if abs(hor1 - kas1) < eps:
                break
    else:
        kas0 = intervals[i][1]
        hor0 = intervals[i][0]
        while abs(hor0 - kas0) > eps:
            kas1 = kas0 - fn(kas0) / dif1(kas0)
            hor1 = hor0 - fn(hor0) * (kas0 - hor0) / (fn(kas0) - fn(hor0))
            kas0 = kas1
            hor0 = hor1
            if abs(hor1 - kas1) < eps:
                break
    print(kas0, hor0)
