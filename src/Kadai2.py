import math

threshold = 10e-15

def func1(x):
    return (x*x*x - 2*x*x + x - 1)

def func2(x):
    return math.cos(x)


def solve_simpson(xmin, xmax, N, func):
    S = 0
    h = (xmax - xmin) / (2 * N)
    x = xmin

    while x < xmax:
        y1 = func(x)
        x += h
        y2 = func(x)
        x += h
        y3 = func(x)

        S += (y1 + 4 * y2 + y3)

    return S * (h / 3)

def find_threshold(xmin, xmax, step, func):
    N = step
    while True:
        v = solve_simpson(xmin, xmax, N, func)
        w = solve_simpson(xmin, xmax, N / 2, func)

        if math.fabs(v - w) <= threshold:
            break
        N += step

    return N
