# voltage and resistances
E = 15

R0 = 1
R1 = 4
R3 = 4
R4 = 5



def make_generator(lower, upper, step):
    """ lowerからupperまで、step刻みでジェネレータを作る """
    i = lower
    while i <= upper:
        yield i
        i += step

def LUDecomposition(matrix, N):
    """INPUT
    matrix: the 2-dimentional matrix you want to decompose into L and U matrix
    the matrix is regarded as square matrix in this function
    N: the size of matrix

    OUTPUT
    L, U: the matrixes decomposed from 'matrix' """


    # make N*N matrix which elements are 0
    L = [[0 for i in range(N)] for j in range(N)]
    U = [[0 for i in range(N)] for j in range(N)]
    # 対角成分を1にする
    for n in range(0, N):
        U[n][n] = 1

    for i in range(N):
        L[i][0] = matrix[i][0] * U[i][i]
    for i in range(1, N):
        U[0][i] = matrix[0][i] / L[0][0]




    return L, U

def solve_wheatstone(lower, upper, step):
    """ ホイートストンブリッジ回路をでとく
    結果をタプルのリストで返す """
    ans = []
    for R2 in make_generator(lower, upper, step):
        # solve Ax = b
        # A: equation_matrix , x: (I1, I2, I3), b: (0, 0, E)

        equation_matrix = ((R1 + R2 + R0,  -R0,          -R2      ),
                          (-R0,            R3 + R4 + R0, -R4      ),
                          (-R2,            -R4,           R2 + R4))
        b = [0, 0, E]


        ans.append((R2, 1))
    return ans

def out_results(results, out_file, digit = 6):
    """ リストの出力 digitに有効桁数を指定　デフォルトで6にしている"""
    with open(out_file, "wt") as f:
        for iter in range(len(results)):
            out_str = "R2 {0[0]:>{1}}R : I0 {0[1]:>{1}}A".format(results[iter], digit)
            print(out_str, file = f)
