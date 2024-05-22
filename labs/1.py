import numpy as np
from sympy import cos, diff, lambdify, symbols


def div_sub_2(x1, x2, f):
    return (f(x2) - f(x1)) / (x2 - x1)


def div_sub_3(x1, x2, x3, f):
    return (div_sub_2(x2, x3, f) - div_sub_2(x1, x2, f)) / (x3 - x1)


def f(x):
    return x / 2 - cos(x / 2)


x, y = symbols("x y")
nums = [0.64]
a, b = 0.4, 0.9


steps = 10
h = (b - a) / steps
points = [round(a + h * i, 10) for i in range(steps + 1)]

result = []

i = 0
for point in points:
    i += 1
    print(i, point, f(point))

print("---------")

for num in nums:
    value = f(num)

    for i in range(len(points) - 1):
        if num >= points[i] and num <= points[i + 1]:
            if i == 0:
                prev = (i - 1, points[0] - h)
            else:
                prev = (i - 1, points[i - 1])
            cur = (i, points[i])
            next = (i + 1, points[i + 1])
            break

    ran = [prev[1], cur[1], next[1]]

    # l1

    l1 = (f(ran[1]) * (num - ran[2]) / (ran[1] - ran[2])) + (
        f(ran[2]) * (num - ran[1]) / (ran[2] - ran[1])
    )

    # r1

    r1_func = lambdify(x, expr=(0.5 * diff(f(x), x, 2)) * (x - ran[1]) * (x - ran[2]))

    local_interv = np.arange(ran[1], ran[2], 10e-6)
    vals = []

    for point in local_interv:
        vals.append(r1_func(point))

    r1 = l1 - f(num)

    r1_min = min(vals)
    r1_max = max(vals)

    print(f"r1_max: {r1_max}", f"r1_min: {r1_min}", f"r1: {r1}", "\n")

    if not (r1 > r1_min and r1 <= r1_max):
        print(f"{num} error. r1 inequality is not correct: {r1_min, r1, r1_max}")

    # l2

    l2 = (
        (
            (f(ran[0]) * (num - ran[1]) * (num - ran[2]))
            / ((ran[0] - ran[1]) * (ran[0] - ran[2]))
        )
        + (
            (f(ran[1]) * (num - ran[0]) * (num - ran[2]))
            / ((ran[1] - ran[0]) * (ran[1] - ran[2]))
        )
        + (
            (f(ran[2]) * (num - ran[0]) * (num - ran[1]))
            / ((ran[2] - ran[0]) * (ran[2] - ran[1]))
        )
    )

    # r2

    r2_func = lambdify(
        x,
        expr=(1 / 6 * diff(f(x), x, 3)) * ((x - ran[0]) * (x - ran[1]) * (x - ran[2])),
    )

    local_interv = np.arange(ran[0], ran[2], 10e-6)
    vals = []

    for point in local_interv:
        vals.append(r2_func(point))

    r2 = l2 - f(num)

    r2_min = min(vals)
    r2_max = max(vals)

    print(f"r2_max: {r2_max}", f"r2_min: {r2_min}", f"r2: {r2}", "\n")

    if not (r2 > r2_min and r2 <= r2_max):
        print(f"{num}: error. r2 inequality is not correct: {r2_min, r2, r2_max}")

    # n1

    n1 = f(ran[1]) + div_sub_2(ran[1], ran[2], f) * (num - ran[1])

    # n2

    n2 = (
        f(ran[0])
        + div_sub_2(ran[0], ran[1], f) * (num - ran[0])
        + div_sub_3(*ran, f) * (num - ran[0]) * (num - ran[1])
    )

    # result

    num_res = {
        num: {
            "f(num)": value,
            "l1": l1,
            "r1": r1,
            "n1": n1,
            "l2": l2,
            "r2": r2,
            "n2": n2,
        }
    }

    result.append(num_res)

    val_4 = round(value, 5)
    val_5 = round(value, 6)

    l1_4 = round(l1, 5)
    l2_5 = round(l2, 6)

    print(f"val: {val_4}", f"l1: {l1_4}", f"sub: {abs(val_4-l1_4)}")
    print(f"val: {val_5}", f"l2: {l2_5}", f"sub: {abs(val_5-l2_5)}\n")

    print(f"n1-l1: {abs(n1-l1)} n2-l2: {abs(n2-l2)}")

    print("\n", num_res, "\n" + "---------")
