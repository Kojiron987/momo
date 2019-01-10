import math

threshold = 10e-10


def func1(x):
    """ 課題１に使う関数 """
    return (x**3 - 2*x**2 + x - 1)

def func2(x):
    """ 課題２に使う関数 """
    return math.cos(x)
def func3(x):
    """検算用"""
    return math.sin(x)

def solve_simpson(x_start, x_end, N, func):
    """ 1/3シンプソンの公式を使い、funcの x_start ~ x_end  までの積分を解く
    Nは、分割数を表す"""

    y0 = func(x_start)
    y_odd = 0.0
    y_even = 0.0
    y2N = func(x_end)

    h = (x_end - x_start) / (2 * N)
    x = x_start
    # 1 ~ N - 1 までのシグマの計算
    for i in range(1, N):
        y_odd  += func(x_start + ((2 * i - 1) * h))
        y_even += func(x_start + ((2 * i)     * h))

    # 奇数倍の方は、N まで計算する
    y_odd += func(x_start + ((2 * N - 1) * h))

    return (h / 3) * (y0 + 4*y_odd + 2*y_even + y2N)

def find_threshold(xmin, xmax, func):
    """ v, wの差の絶対値が threshold 以下になる分割数 'N' を10の倍数ごとに探す関数 """

    N = 10
    while True:
        v = solve_simpson(xmin, xmax, N, func)
        w = solve_simpson(xmin, xmax, int(N / 2), func)

        if math.fabs(v - w) <= threshold:
            break
        N *= 10

    return N


def out_results(result1, result2, out_file):
    """ 結果の出力 """
    with open(out_file, "wt") as fout:
        print(f"func1: {result1}", file = fout)
        print(f"func2: {result2}", file = fout)
