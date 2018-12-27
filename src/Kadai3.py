def circuit1(t, v):
    """ 回路1の微分方程式
    dv/dt = -v/RC + E/RC
    """
    E = 10
    R = 50 * 1000
    C = 200 * 10.0e-6

    return (-v + E) / (R * C)

def circuit2(t, i):
    """ プログラムがあっているかの確認用回路 """
    return 1 - t


def solve_4d_runge_kutta(y0, x_start, x_end, h, equation):
    """ 4次のルンゲ・クッタ法で微分方程式を解く
    y0: x = tminのときの値
    x_start: xの初期値
    x_end: どこまで計算するか
    h: 刻み値
    equation: 計算に使う回路"""

    x = x_start
    y = y0

    # リストに結果を格納
    x_out = [x]
    y_out = [y]

    while x < x_end:

        k1 = h * equation(x, y)
        k2 = h * equation(x+(h/2), y+(k1/2))
        k3 = h * equation(x+(h/2), y+(k2/2))
        k4 = h * equation(x+h, y+k3)

        y = y + (1 / 6) * (k1 + 2*k2 + 2*k3 + k4)
        x += h

        x_out.append(x)
        y_out.append(y)

    return x_out, y_out

def plot_graph(x_arr, y_arr):

    import matplotlib.pyplot as plt

    plt.title("kadai3")
    plt.xlabel("time")
    plt.ylabel("voltage")
    plt.plot(x_arr, y_arr)
    plt.show() # グラフにして出力

def save_graph(x_arr, y_arr, out_file):
    import matplotlib.pyplot as plt


    plt.title("kadai3")
    plt.xlabel("time")
    plt.ylabel("voltage")
    plt.plot(x_arr, y_arr)
    plt.savefig(out_file)
