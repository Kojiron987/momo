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

    import Kadai2

    out_file = "../result/ans_Kadai1.txt"



elif kadai == 'kadai3':
    out_file = "../result/ans_Kadai1.txt"

else:
    print("Invaild Option")
    print(f"Usage: python3.x {script} kadai(123)")
