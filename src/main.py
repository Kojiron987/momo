import  sys

script, kadai = sys.argv

if kadai == 'kadai1':
    import Kadai1

    out_file = "../result/ans_Kadai1.txt"

    lower = 0
    upper = 10
    step = 0.5

    results = Kadai1.solve_wheatstone(lower, upper, step)

    Kadai1.out_results(results, out_file)


elif kadai == 'kadai2':

    import Kadai2, math

    out_file = "../result/ans_Kadai1.txt"

    xmin = -2
    xmax = 3
    N = 100000
    func = Kadai2.func1
    result1 = Kadai2.find_threshold(xmin, xmax, func)
    print(f"func1 {result1}")

    xmin = 0
    xmax = math.pi / 2
    N = 100
    func = Kadai2.func2
    result2 = Kadai2.find_threshold(xmin, xmax, func)
    print(f"func2 {result2}")

elif kadai == 'kadai3':
    out_file = "../result/ans_Kadai1.txt"

else:
    print("Invaild Option")
    print(f"Usage: python3.x {script} kadai(123)")
