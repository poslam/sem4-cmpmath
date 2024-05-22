import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f, norm, t


def draw(t_n, t_crit, p_value):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axvline(t_n, color="green", label=f"t_n:{t_n}")
    ax.axvline(t_crit, color="red", label=f"t_crit:{t_crit}")
    ax.axvline(p_value, color="purple", label=f"p_value:{p_value}")
    ax.axvline(-t_crit, color="red")
    x = np.linspace(t_n - 7, t_n + 15, 1000)
    y = norm.pdf(x)
    plt.plot(x, y)
    ax.legend()
    ax.fill_between(
        x, 0, y, where=(x >= t_crit) | (x <= -t_crit), alpha=0.5, color="red"
    )
    plt.show()


def large_samples_test(
    n1: int,
    n2: int,
    mean1: float,
    mean2: float,
    var1: float,
    var2: float,
    alpha: float,
    type: int,
):
    z = (mean1 - mean2) / (np.sqrt(var1 / n1 + var2 / n2))
    if type == -1:
        p_value = 1 - norm.cdf(z)
        z_crit = norm.ppf((1 - 2 * alpha) / 2)
        if z > -z_crit:
            print("Нет оснований отвергнуть нулевую гипотезу")
        else:
            print("Нулевая гипотеза отвержена")
        draw(z, z_crit, p_value)
    elif type == 1:
        p_value = 1 - norm.cdf(z)
        z_crit = norm.ppf((1 - 2 * alpha) / 2)
        if z < z_crit:
            print("Нет оснований отвергнуть нулевую гипотезу")
        else:
            print("Нулевая гипотеза отвержена")
        draw(z, z_crit, p_value)
    else:
        p_value = 2 * (1 - norm.cdf(z))
        z_crit = norm.ppf(1 - alpha / 2)
        if abs(z) < z_crit:
            print("Нет оснований отвергнуть нулевую гипотезу")
        else:
            print("Нулевая гипотеза отвержена")
        draw(z, z_crit, p_value)


def fisher_test(n1: int, n2: int, var1: float, var2: float, alpha: float, type: int):
    f_n = max(var1, var2) / min(var1, var2)
    k1, k2 = 0, 0
    if max(var1, var2) == var1:
        k1 = n1 - 1
        k2 = n2 - 1
    else:
        k1 = n2 - 1
        k2 = n1 - 1
    if type == 1:
        p_value = 2 * (1 - f.cdf(f_n, k1, k2))
        f_crit = f.ppf(1 - alpha / 2, k1, k2)
        if f_n < f_crit:
            print("Нет оснований отвергнуть нулевую гипотезу")
        else:
            print("Нулевая гипотеза отвержена")
        draw(f_n, f_crit, p_value)
    elif type == 0:
        p_value = 1 - f.cdf(abs(f_n), k1, k2)
        f_crit = f.ppf(1 - alpha, k1, k2)
        if f_n < f_crit:
            print("Нет оснований отвергнуть нулевую гипотезу")
        else:
            print("Нулевая гипотеза отвержена")
        draw(f_n, f_crit, p_value)
    else:
        p_value = 1 - f.cdf(f_n, k1, k2)
        f_crit = f.ppf(1 - alpha, k1, k2)
        if f_n > -f_crit:
            print("Нет оснований отвергнуть нулевую гипотезу")
        else:
            print("Нулевая гипотеза отвержена")
        draw(f_n, f_crit, p_value)
    return


def student_test(
    n1: int,
    n2: int,
    mean1: float,
    mean2: float,
    var1: float,
    var2: float,
    alpha: float,
    type: int,
):
    if fisher_test(n1, n2, var1, var2, alpha, type) == 0:
        print("Фишер не выполняется")
        return 0
    t_n = ((mean1 - mean2) / np.sqrt((n1 - 1) * var1 + (n2 - 1) * var2)) * np.sqrt(
        n1 * n2 * (n1 + n2 - 2) / (n1 + n2)
    )
    k = n1 + n2 - 2
    if type == 1:
        p_value = 1 - t.cdf(t_n, k)
        t_crit = t.ppf(1 - alpha, k)
        if abs(t_n) < t_crit:
            print("Нет оснований отвергнуть нулевую гипотезу")
        else:
            print("Нулевая гипотеза отвержена")
        draw(t_n, t_crit, p_value)
    elif type == 0:
        p_value = 2 * (1 - t.cdf(abs(t_n), k))
        t_crit = t.ppf(1 - alpha / 2, k)
        if t_n < t_crit:
            print("Нет оснований отвергнуть нулевую гипотезу")
        else:
            print("Нулевая гипотеза отвержена")
        draw(t_n, t_crit, p_value)

    else:
        p_value = 1 - t.cdf(t_n, k)
        t_crit = t.ppf(alpha, k)
        if t_n > -t_crit:
            print("Нет оснований отвергнуть нулевую гипотезу")
        else:
            print("Нулевая гипотеза отвержена")
        draw(t_n, t_crit, p_value)


if __name__ == "__main__":
    # large_samples_test(50, 50, 20.1, 19.8, 1.750, 1.375, 0.05, 0)
    # fisher_test(14, 10, 0.84, 2.52, 0.1, 0)
    student_test(10, 8, 142.3, 145.3, 2.7, 3.2, 0.01, 0)
