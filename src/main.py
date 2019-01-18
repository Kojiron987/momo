import  sys

def print_error(script = "main.py"):
    """ print how to use this program """
    
    error_message = f"""Usage: python3 {script} kadai2
        or
Usage: python3 {script} kadai3"""

    print("Invaild Option")
    print(error_message)

    sys.exit(0)




# 引数が一つでないとき
if len(sys.argv) != 2:
    print_error(script = sys.argv[0])

script, kadai = sys.argv


if kadai == 'kadai2':

    import Kadai2, math

    out_file = "../result/Kadai2.txt"

    xmin = -2
    xmax = 3
    func = Kadai2.func1
    result1 = Kadai2.find_threshold(xmin, xmax, func)


    x_start = 0
    x_end = math.pi / 2
    func = Kadai2.func2
    result2 = Kadai2.find_threshold(x_start, x_end, func)

    Kadai2.out_results(result1, result2, out_file)

elif kadai == 'kadai3':

    import Kadai3

    out_file1 = "../result/Kadai3_input.png"
    out_file2 = "../result/Kadai3_output.png"
    out_file3 = "../result/Kadai3_in_and_output.png"


    v_init = 0.0
    t_start = 0.0
    t_end = 5.0
    h = 0.01
    circuit = Kadai3.circuit1

    t, v_in, v_out = Kadai3.solve_4d_runge_kutta(v_init, t_start, t_end, h, circuit)


    Kadai3.save_graph(t, v_in, out_file1)
    Kadai3.plot_graph(t, v_in)

    Kadai3.save_graph(t, v_out, out_file2)
    Kadai3.plot_graph(t, v_out)

    Kadai3.save_graph(t, v_in, out_file1)
    Kadai3.save_graph(t, v_out, out_file3)

else:
    print_error(script = sys.argv[0])
