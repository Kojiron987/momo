import  sys

script, kadai = sys.argv

if kadai == 'kadai1':
    import Kadai1

    out_file = "../resultKadai1.txt"

    lower = 0
    upper = 10
    step = 0.5

    results = Kadai1.solve_wheatstone(lower, upper, step)

    Kadai1.out_results(results, out_file)


elif kadai == 'kadai2':

    import Kadai2, math

    out_file = "../result/Kadai2.txt"

    xmin = -2
    xmax = 3
    func = Kadai2.func1
    result1 = Kadai2.find_threshold(xmin, xmax, func)

    xmin = 0
    xmax = math.pi / 2
    func = Kadai2.func2
    result2 = Kadai2.find_threshold(xmin, xmax, func)

    Kadai2.out_results(result1, result2, out_file)

elif kadai == 'kadai3':
    out_file = "../result/Kadai3.txt"

else:
    print("Invaild Option")
    print(f"Usage: python3.x {script} kadai(123)")
