def circuit1(t, v):
    """ 回路1の微分方程式
    dv/dt = -v/RC + E/RC
    """
    R = 50 * 1000
    C = 5 * 10.0e-6
    E = input_wave(t)
    return (-v + E) / (R * C)

def circuit2(t, i):
    """ プログラムがあっているかの確認用回路 """
    return 1 - t

def input_wave(x):
    if x - int(x) < 0.5:
        return 20
    else:
        return 0


def solve_4d_runge_kutta(y0, x_start, x_end, h, equation):
    """ 4次のルンゲ・クッタ法で微分方程式を解く
    y0: x = x_start のときの値
    x_start: xの初期値
    x_end: どこまで計算するか
    h: 刻み値
    equation: 計算に使う回路(関数)"""


    # リストに結果を格納
    x_out = [x_start]
    y_out = [y0]

    # 時間tをリストにする
    time = [x_start + (h * i) for i in range(0, int((x_end - x_start) / h))]

    # 入力の矩形波を作る
    y_input = [input_wave(i) for i in time]

    y = y0
    x = x_start

    # 4次のルンゲクッタを解く
    # x = x_start のときのyはすでに計算済み
    for x in time[1:]:
        k1 = h * equation(x, y)
        k2 = h * equation(x+(h/2), y+(k1/2))
        k3 = h * equation(x+(h/2), y+(k2/2))
        k4 = h * equation(x+h, y+k3)

        y = y + (1 / 6) * (k1 + 2*k2 + 2*k3 + k4)

        y_out.append(y)

    # 時間t, 入力波形、出力波形をリストにして返す
    return time, y_input, y_out

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
