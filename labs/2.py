import math

import numpy as np


def fn(x) -> float:
    return x**2 + np.log(x)


def binSearch(value, list) -> int:
    if value < list[0]:
        return -1
    elif value > list[len(list) - 1]:
        return -1
    else:
        left = 0
        right = len(list) - 1
        while left < right - 1:
            mid = (right + left) // 2
            if value >= list[mid]:
                left = mid
            else:
                right = mid
        return left


def t_search(x, x0, step) -> float:
    return (x - x0) / step


def array_transform(x, xi: list) -> list:
    left_index = binSearch(x, xi)
    right_index = left_index + 1

    if abs(xi[left_index] - x) < abs(xi[right_index] - x):
        x0 = xi[left_index]
    else:
        x0 = xi[right_index]

    if x0 == xi[0] or x0 == xi[1]:
        return xi
    elif x0 == xi[-1] or x0 == xi[-2]:
        return xi[::-1]
    elif x0 == xi[left_index]:
        new_list = [x0]
        step = 1
        i = 1
        length = len(xi)
        while i < length:
            if i % 2 != 0 and left_index + step < len(xi):
                new_list.append(xi[left_index + step])
            elif left_index - step >= 0:
                new_list.append(xi[left_index - step])
                step += 1
            else:
                step += 1
                length += 1
            i += 1
        return new_list
    elif x0 == xi[right_index]:
        new_list = [x0]
        step = 1
        i = 1
        length = len(xi)
        while i < length:
            if i % 2 != 0 and right_index - step >= 0:
                new_list.append(xi[right_index - step])
            elif right_index + step < len(xi):
                new_list.append(xi[right_index + step])
                step += 1
            else:
                step += 1
                length += 1
            i += 1
        return new_list


def finite_differences(xs: list, n) -> float:
    a = xs[0]
    if n == 0:
        return a

    new_list = []
    for i in range(len(xs) - 1):
        new_list.append(xs[i + 1] - xs[i])

    a = finite_differences(new_list, n - 1)
    return a


def newtone_1(xs: list, t) -> float:
    answer = xs[0]
    for i in range(1, len(xs)):
        product = 1
        for j in range(i):
            product *= t - j
        answer += (product) / (math.factorial(i)) * finite_differences(xs, i)
    return answer


def newtone_2(xs: list, t) -> float:
    answer = xs[0]
    for i in range(1, len(xs)):
        product = 1
        for j in range(i):
            product *= t + j
        answer += (product) / (math.factorial(i)) * abs(finite_differences(xs, i))
    return answer


def gauss_1(xs: list, t) -> float:
    t1 = t
    numerator = 1
    formula = 0
    for i in range(len(xs) - 1):
        for j in range(i):
            t1 += j * (-1) ** j
            numerator *= t1
        formula += numerator / (math.factorial(i)) * finite_differences(xs, i)
        t1 = t
        numerator = 1
    return formula


def gauss_2(xs: list, t) -> float:
    t1 = t
    numerator = 1
    formula = 0
    for i in range(len(xs) - 1):
        for j in range(i):
            t1 += (-1) * j * (-1) ** j
            numerator *= t1
        formula += numerator / (math.factorial(i)) * abs(finite_differences(xs, i))
        t1 = t
        numerator = 1
    return formula


# Ввод границ и точек
a, b = 0.4, 0.9
h = (b - a) / 10
xi = [(a + i * h) for i in range(11)]
x_star = [0.42, 0.84, 0.56, 0.675]

# Определение близжайшей точки к x*
left_index = binSearch(x_star[2], xi)
right_index = left_index + 1

if abs(xi[left_index] - x_star[2]) < abs(xi[right_index] - x_star[2]):
    x0 = xi[left_index]
else:
    x0 = xi[right_index]

# Определение параметра t, трансформирование массива для разностей только вперед для x**
t1 = t_search(x_star[0], xi[0], h)
xs1 = array_transform(x_star[0], xi)
list_of_functions1 = [fn(xs1[i]) for i in range(len(xs1))]

print(newtone_1(list_of_functions1, t1))
print(fn(x_star[0]))

# Определение параметра t, трансформирование массива для разностей только вперед для x***
t2 = t_search(x_star[1], xi[-1], h)
xs2 = array_transform(x_star[1], xi)
list_of_functions2 = [fn(xs2[i]) for i in range(len(xs2))]

print(newtone_2(list_of_functions2, t2))
print(fn(x_star[1]))

# Определение параметра t, трансформирование массива для разностей только вперед для x****
t3 = t_search(x_star[2], x0, h)
xs3 = array_transform(x_star[2], xi)
list_of_functions3 = [fn(xs3[i]) for i in range(len(xs3))]

print(gauss_1(list_of_functions3, t3))
print(fn(x_star[2]))

# Определение параметра t, трансформирование массива для разностей только вперед для x*****
left_index1 = binSearch(x_star[3], xi)
right_index1 = left_index1 + 1

if abs(xi[left_index1] - x_star[3]) < abs(xi[right_index1] - x_star[3]):
    x1 = xi[left_index1]
else:
    x1 = xi[right_index1]

t4 = t_search(x_star[3], x1, h)
xs4 = array_transform(x_star[3], xi)
list_of_functions4 = [fn(xs4[i]) for i in range(len(xs4))]

print(gauss_2(list_of_functions4, t4))
print(fn(x_star[3]))
