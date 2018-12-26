import math

threshold = 10e-10

# FIXME: func1だと、find_threshold関数で Nが100000になっても誤差がthreshold
# 以下に収まらず、hが増え続けるため誤差が大きくなり、無限ループにはまってしまう

def func1(x):
    return (x**3 - 2*x**2 + x - 1)

def func2(x):
    return math.cos(x)


def solve_simpson(xmin, xmax, N, func):
    h = (xmax - xmin) / (2 * N)
    x = xmin

    y0 = func(xmin)
    y_odd = 0
    y_even = 0
    y2N = func(xmax)

    for i in range(1, N - 1):
        x += h
        y_odd += func(x)

        x += h
        y_even += func(x)

    x += h
    y_odd += func(x)


    return (h / 3) * (y0 + 4*y_odd + 2*y_even + y2N)

def find_threshold(xmin, xmax, func):
    N = 10
    while True:
        v = solve_simpson(xmin, xmax, N, func)
        w = solve_simpson(xmin, xmax, int(N / 2), func)

        if math.fabs(v - w) <= threshold:
            break
        N *= 10

    return N
