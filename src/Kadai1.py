import math
# voltage and resistances

R0 = 1
R1 = 4
R3 = 4
R4 = 5

E = 15


def make_generator(lower, upper, step):
    """ lowerからupperまで、step刻みでジェネレータを作る """
    i = lower
    while i <= upper:
        yield i
        i += step



def solve_wheatstone(lower, upper, step):
    """ ホイートストンブリッジ回路をLU分解でとく
    結果をタプルのリストで返す """
    ans = []
    for R2 in make_generator(lower, upper, step):
        # solve Ax = b
        # A: equation_matrix , x: (I1, I2, I3), b: (0, 0, E)
        equation_matrix = [[R1 + R2 + R0,  -R0,          -R2],
                          [-R0,            R3 + R4 + R0, -R4],
                          [-R2,            -R4,           R2 + R4]]
        b = [0, 0, E]


        ans.append((R2, 1))
    return ans

def out_results(results, out_file, digit = 6):
    """ リストの出力 digitに有効桁数を指定　デフォルトで6にしている"""
    with open(out_file, "wt") as f:
        for iter in range(len(results)):
            out_str = "R2 {0[0]:>{1}}R : I0 {0[1]:>{1}}A".format(results[iter], digit)
            print(out_str, file = f)





def LUPDecompose(A, N, Tol, P):
    """　行列AをLUP分解する　"""

    for i in range(0, N + 1):
        P[i] = i

    for i in range(0, N):
        maxA = 0.0
        imax = i

        for k in range(i, K):
            if (absA = math.fabs(A[k][i])) > maxA:
                maxA = absA
                imax = k

        #if maxA < Tol: sys.exit() # failure

        if imax != i:
            # pivoting P
            j = P[i]
            P[i] = P[imax]
            P[imax] = j

            # pivoting rows of A
            ptr = A[i]
            A[i] = A[imax]
            A[imax] = ptr

            # counting pivots starting from N
            P[N] += 1

        for j in range(i + 1, N):
            A[j][i] /= A[i][j]

            for k in range(i + 1, N):
                A[j][k] -= A[ji] * A[i][k]
