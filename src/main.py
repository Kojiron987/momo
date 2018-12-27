import  sys

script, kadai = sys.argv

if kadai == 'kadai1':
    import Kadai1

    out_file = "../result/Kadai1.txt"

    lower = 0
    upper = 10
    step = 0.5

    results = Kadai1.solve_wheatstone(lower, upper, step)

    Kadai1.out_results(results, out_file)


elif kadai == 'kadai2':

    import Kadai2, math

    out_file = "../result/Kadai2.txt"

    #bug
    #xmin = -2
    #xmax = 3
    #func = Kadai2.func1
    #result1 = Kadai2.find_threshold(xmin, xmax, func)

    result1 = 0

    x_start = 0
    x_end = math.pi / 2
    func = Kadai2.func2
    result2 = Kadai2.find_threshold(x_start, x_end, func)

    Kadai2.out_results(result1, result2, out_file)

elif kadai == 'kadai3':

    import Kadai3

    out_file = "../result/Kadai3.png"

    v_init = 0.0
    t_start = 0.0
    t_end = 2.0
    h = 0.001
    circuit = Kadai3.circuit1

    t, v = Kadai3.solve_4d_runge_kutta(v_init, t_start, t_end, h, circuit)

    Kadai3.plot_graph(t, v)
    Kadai3.save_graph(t, v, out_file)


else:
    print("Invaild Option")
    print(f"Usage: python3.x {script} kadai(123)")
