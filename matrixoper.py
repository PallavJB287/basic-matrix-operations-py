print("Enter the no. of rows:")
r = int(input())
print("Enter the no. of columns:")
c = int(input())
mat = []
print("Enter the elements row-wise:")
for i in range(r):
    t = list(map(int, input().split(" ")))
    mat.append(t)


def coloper(mat, c1, n1, c2, n2, op):
    co1, co2 = c1-1, c2-1
    if op == "+":
        for i in range(c):
            mat[i][co1] = n1*mat[i][co1]+n2*mat[i][co2]
    elif op == "-":
        for i in range(c):
            mat[i][co1] = n1*mat[i][co1]-n2*mat[i][co2]
    return mat


def rowoper(mat, r1, n1, r2, n2, op):
    ro1, ro2 = r1-1, r2-1
    if op == "+":
        for i in range(r):
            mat[ro1][i] = n1*mat[ro1][i]+n2*mat[ro2][i]
    elif op == "-":
        for i in range(r):
            mat[ro1][i] = n1*mat[ro1][i]-n2*mat[ro2][i]
    return mat


def rowswap(mat, r1, r2):
    ro1, ro2 = r1-1, r2-1
    for i in range(r):
        mat[ro1][i], mat[ro2][i] = mat[ro2][i], mat[ro1][i]


def colswap(mat, c1, c2):
    co1, co2 = c1-1, c2-1
    for i in range(c):
        mat[i][co1], mat[i][co2] = mat[i][co2], mat[i][co1]


def showres(mat):
    print("The matrix is:")
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end=" ")
        print("")


print("Available operations:\n1. Row addition/subtraction\n2. Column addition/subtraction\n3. Row swapping\n4. Column swapping\nYour choice:")
oper = int(input())
if oper == 1:
    res = False
    while(res == False):
        print("Enter the values of r1, n1, r2, n2:")
        t = list(map(float, input().split(" ")))
        print("Choose operation:")
        op = input()
        if op == "+":
            rowoper(mat, int(t[0]), t[1], int(t[2]), t[3], "+")
        elif op == "-":
            rowoper(mat, int(t[0]), t[1], int(t[2]), t[3], "-")
        showres(mat)
        print("End the process?")
        a = input()
        if a == "yes":
            res = True
        elif a == "no":
            res = False
elif oper == 2:
    res = False
    while(res == False):
        print("Enter the values of c1, n1, c2, n2:")
        t = list(map(float, input().split(" ")))
        print("Choose operation:")
        op = input()
        if op == "+":
            coloper(mat, int(t[0]), t[1], int(t[2]), t[3], "+")
        elif op == "-":
            coloper(mat, int(t[0]), t[1], int(t[2]), t[3], "-")
        showres(mat)
        print("End the process?")
        a = input()
        if a == "yes":
            res = True
        elif a == "no":
            res = False
elif oper == 3:
    res = False
    while(res == False):
        print("Enter the values of r1 and r2:")
        t = list(map(int, input().split(" ")))
        rowswap(mat, t[0], t[1])
        showres(mat)
        print("End the process?")
        a = input()
        if a == "yes":
            res = True
        elif a == "no":
            res = False
elif oper == 4:
    res = False
    while(res == False):
        print("Enter the values of c1 and c2:")
        t = list(map(int, input().split(" ")))
        colswap(mat, t[0], t[1])
        showres(mat)
        print("End the process?")
        a = input()
        if a == "yes":
            res = True
        elif a == "no":
            res = False

print("The final matrix is:")
for i in range(r):
    for j in range(c):
        print(mat[i][j], end=" ")
    print("")
