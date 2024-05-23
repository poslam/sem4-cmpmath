import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2 + np.log(x)


def f_prime(x):
    return 2 * x + 1 / x


def lagrange_derivative(target_x):
    keys = list(d.keys())
    for i in range(len(keys) - 1):
        if keys[i] <= target_x <= keys[i + 1]:
            x_i, xi_1, xi_11 = keys[i], keys[i + 1], keys[i - 1]
            f_i, fi_1, fi_11 = d[x_i], d[xi_1], d[xi_11]
            L_derivative = (
                f_i * (2 * target_x - xi_1 - xi_11) / ((x_i - xi_1) * (x_i - xi_11))
                + fi_1 * (2 * target_x - x_i - xi_11) / ((xi_1 - x_i) * (xi_1 - xi_11))
                + fi_11 * (2 * target_x - x_i - xi_1) / ((xi_11 - x_i) * (xi_11 - xi_1))
            )
            return L_derivative
    return None


target_x_1 = 0.52
a = 0.4
b = 0.9

d = dict()
h = (b - a) / 10
for i in range(11):
    xi = a + i * h
    d[xi] = f(xi)


x_values = np.linspace(a, b, 100)

y_values_L = [lagrange_derivative(x) for x in x_values]
y_values_f = [f_prime(x) for x in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_L, label="L'(x)")
plt.plot(x_values, y_values_f, label="f'(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of L'(x) and f'(x)")
plt.grid(True)
plt.show()

print("L'(x):", lagrange_derivative(target_x_1))
print("f'(x):", 2 * target_x_1 + 1 / target_x_1)
print(
    "f'(x) - L'(x) = ",
    (2 * target_x_1 + 1 / target_x_1) - lagrange_derivative(target_x_1),
)
