def solver(a: list, b: list, c: list, f: list) -> list:
    for i in range(1, len(b)):
        b[i] = b[i] - (a[i] / b[i - 1]) * c[i - 1]
        f[i] = f[i] - (a[i] / b[i - 1]) * f[i - 1]

    x = [0] * len(b)
    x[len(x) - 1] = f[len(f) - 1] / b[len(b) - 1]

    for i in range(len(b) - 2, -1, -1):
        x[i] = (f[i] - c[i] * x[i + 1]) / b[i]

    return x[::-1]


if __name__ == "__main__":
    a = [0, -1, 7, 4, -5]
    b = [8, 5, -5, 7, 8]
    c = [-2, 3, -9, 9, 0]
    f = [-7, 6, 9, -8, 5]

    print(solver(a, b, c, f))
