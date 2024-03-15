# 24

import numpy as np
from sympy import cos, diff, lambdify, symbols

x, y = symbols("x y")

basic_precision = 10


def f(x):
    return x / 2 - cos(x)


def dif(func, deg=1):
    for _ in range(deg):
        func = diff(func)
    return func


nums = [0.64, 0.42, 0.87, 0.63]
a, b = 0.4, 0.9
steps = 10

h = (b - a) / steps
points = [round(a + h * i, basic_precision) for i in range(steps + 1)]

result = []

for num in nums:
    for i in range(len(points) - 1):
        if num >= points[i] and num <= points[i + 1]:
            if i == 0:
                prev = (i - 1, points[0] - h)
            else:
                prev = (i - 1, points[i - 1])
            cur = (i, points[i])
            next = (i + 1, points[i + 1])
            break

    # l1

    l1 = (f(cur[1]) * (num - next[1]) / (cur[1] - next[1])) + (
        f(next[1]) * (num - cur[1]) / (next[1] - cur[1])
    )

    # r1

    r1_func = lambdify(x, expr=(0.5 * dif(f(x), 2)) * (num - cur[1]) * (num - next[1]))

    local_interv = np.arange(cur[1], next[1], 10e-4)
    vals = []

    for point in local_interv:
        vals.append(r1_func(point))

    r1 = l1 - f(num)

    r1_min = min(vals)
    r1_max = max(vals)

    if not (r1 > r1_min and r1 <= r1_max):
        print(f"{num} error. r1 inequality is not correct: {r1_min, r1, r1_max}")

    # l2

    l2 = (
        (
            (f(prev[1]) * (num - cur[1]) * (num - next[1]))
            / ((prev[1] - cur[1]) * (prev[1] - next[1]))
        )
        + (
            (f(cur[1]) * (num - prev[1]) * (num - next[1]))
            / ((cur[1] - prev[1]) * (cur[1] - next[1]))
        )
        + (
            (f(next[1]) * (num - prev[1]) * (num - cur[1]))
            / ((next[1] - prev[1]) * (next[1] - cur[1]))
        )
    )

    # r2

    r2_func = lambdify(
        x,
        expr=(1 / 6 * dif(f(x), 3))
        * ((num - prev[1]) * (num - cur[1]) * (num - next[1])),
    )

    local_interv = np.arange(prev[1], next[1], 10e-4)
    vals = []

    for point in local_interv:
        vals.append(r2_func(point))

    r2 = l2 - f(num)

    r2_min = min(vals)
    r2_max = max(vals)

    if not (r2 > r2_min and r2 <= r2_max):
        print(f"{num}: error. r2 inequality is not correct: {r2_min, r2, r2_max}")

    # n1

    n1 = f(cur[1]) + (f(cur[1]) - f(next[1]) / (cur[1] - next[1])) * (num - cur[1])

    # n2

    n2 = (
        f(prev[1])
        + (f(prev[1]) - f(cur[1]) / (prev[1] - cur[1])) * (num - prev[1])
        + (
            (f(prev[1]) + f(cur[1]) + f(next[1]))
            / (
                (prev[1] - cur[1])
                * (prev[1] - next[1])
                * (cur[1] - prev[1])
                * (cur[1] - next[1])
                * (next[1] - cur[1])
                * (next[1] - prev[1])
            )
        )
        * (num - prev[1])
        * (num - cur[1])
    )

    # result

    num_res = {num: {"l1": l1, "r1": r1, "n1": n1, "l2": l2, "r2": r2, "n2": n2}}

    print()

    print(num_res)

    result.append(num_res)

    print("---------")
