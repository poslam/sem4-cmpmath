import numpy as np
from scipy.integrate import quad


def f(x):
    return np.sin(x)


def int_f(a, b):
    return -np.cos(b) + np.cos(a)


def left_rectangles(f, a, b, n):
    sum = 0
    for i in range(n):
        sum += f(a + i * h)
    return h * sum


def right_rectangles(f, a, b, n):
    sum = 0
    for i in range(1, n + 1):
        sum += f(a + i * h)
    return h * sum


def central_rectangles(f, a, b, n):
    sum = 0
    for i in range(n):
        sum += f(a + (i + 0.5) * h)
    return h * sum


def trapezoid(f, a, b, n):
    sum = 0
    for i in range(n):
        sum += f(a + i * h)
    return h * (0.5 * f(a) + sum + 0.5 * f(b))


def simpson(f, a, b, n):
    sum = f(a) + f(b)
    for i in range(1, n):
        sum += 2 * f(a + i * h)
    for j in range(0, n):
        sum += 4 * f(a + (j + 0.5) * h)
    return h * sum / 6


def weddle(f, a, b, n):
    sum = 0

    for i in range(0, n + 1, 6):
        sum += (
            f(a + i * h)
            + 5 * f(a + (i + 1) * h)
            + f(a + (i + 2) * h)
            + 6 * f(a + (i + 3) * h)
            + f(a + (i + 4) * h)
            + 5 * f(a + (i + 5) * h)
            + 2 * f(a + (i + 6) * h)
        )

    return 3 * h / 10 * sum


def newton_cotes(f, a, b, n, ck):
    sum = 0
    for k in range(n + 1):
        sum += ck[k] * f(a + k * h)
    return (b - a) * sum


def gauss(f, a, b, n, tk, ck):
    sum = 0
    for k in range(1, n + 1):
        xk = (b + a) / 2 + (b - a) / 2 * tk[k - 1]
        sum += ck[k - 1] * f(xk)
    return (b - a) / 2 * sum


a = 0
b = 1
n = 10
h = (b - a) / n


res_left = left_rectangles(f, a, b, n)
res_right = right_rectangles(f, a, b, n)
res_central = central_rectangles(f, a, b, n)
res_trapezoid = trapezoid(f, a, b, n)
res_simpson = simpson(f, a, b, n)
res_weddle = weddle(f, a, b, n)

res_nc_1 = newton_cotes(f, a, b, 1, [1 / 2, 1 / 2])
res_nc_2 = newton_cotes(f, a, b, 2, [1 / 6, 4 / 6, 1 / 6])
res_nc_3 = newton_cotes(f, a, b, 3, [1 / 8, 3 / 8, 3 / 8, 1 / 8])
res_nc_4 = newton_cotes(f, a, b, 4, [7 / 90, 32 / 90, 12 / 90, 32 / 90, 7 / 90])
res_nc_5 = newton_cotes(
    f, a, b, 5, [19 / 288, 75 / 288, 50 / 288, 50 / 288, 75 / 288, 19 / 288]
)
res_nc_6 = newton_cotes(
    f,
    a,
    b,
    6,
    [41 / 840, 216 / 840, 27 / 840, 272 / 840, 27 / 840, 216 / 840, 41 / 840],
)

res_gauss1 = gauss(f, a, b, 1, [0], [2])
res_gauss2 = gauss(f, a, b, 2, [-0.577350, 0.577350], [1, 1])
res_gauss3 = gauss(f, a, b, 3, [-0.774597, 0, 0.774597], [5 / 9, 8 / 9, 5 / 9])
res_gauss4 = gauss(
    f,
    a,
    b,
    4,
    [-0.861136, -0.339981, 0.339981, 0.861136],
    [0.347855, 0.652145, 0.652145, 0.347855],
)

res, err = quad(f, a, b)

print("1. Левые прямоугольники: ", res_left)
print("2. Правые прямоугольники: ", res_right)
print("3. Центральные прямоугольники: ", res_central)
print("4. Трапеции: ", res_trapezoid)
print("5. Симпсон: ", res_simpson)
print("6. Веддль: ", res_weddle)
print("7. Ньютон-Котес, n = 1:", res_nc_1)
print("8. Ньютон-Котес, n = 2:", res_nc_2)
print("9. Ньютон-Котес, n = 3:", res_nc_3)
print("10. Ньютон-Котес, n = 4:", res_nc_4)
print("11. Ньютон-Котес, n = 5:", res_nc_5)
print("12. Ньютон-Котес, n = 6:", res_nc_6)
print("13. Гаусс, n = 1: ", res_gauss1)
print("14. Гаусс, n = 2: ", res_gauss2)
print("15. Гаусс, n = 3: ", res_gauss3)
print("16. Гаусс, n = 4: ", res_gauss4)
print("Истинное значение интеграла: ", res)
print("Разница между истинным и Гауссом при n=4", int_f(a, b) - res_gauss4)
