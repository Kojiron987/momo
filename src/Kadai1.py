import sympy

# voltage and resistances
E = 15
R0 = 1
R1 = 4
R3 = 4
R4 = 5

# other variables
I0_list = []
out_file = "../result/Kadai1.txt"

# register symbols for resolving equation
I1, I2, I3 = sympy.symbols('I1 I2 I3')
sympy.init_printing()

# make generator
R2_gene = (i / 2 for i in range(0, 21))

for R2 in R2_gene:
    # assign electorical resistance to R2
    expr1 = (R1 + R2 + R0) * I1 - R0 * I2 - R2 * I3
    expr2 = -R0 * I1 + (R3 + R4 + R0) * I2 - R4 * I3
    expr3 = -R2 * I1 - R4 * I2 + (R2 + R4) * I3 - E

    # solve equation
    ans = sympy.solve([expr1, expr2, expr3], [I1, I2, I3])

    # add answer to list
    I0_list.append((R2, ans[I1] - ans[I2]))

# write results to out_file
with open(out_file, "wt") as fout:
    digit = 6
    enabled_digit = 10

    for iter in I0_list:
        I0_formatted = (str(iter[1]))[:enabled_digit]
        out_str = f"R2 {iter[0]:>{digit}}R : I0 {I0_formatted:>{digit}}A"
        print(out_str, file = fout)
