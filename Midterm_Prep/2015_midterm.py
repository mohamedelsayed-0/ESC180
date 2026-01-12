def print_first_half(L):
    index = len(L)
    while index > 2:
        index -= 1
        L.pop()
    return L

print(print_first_half(["pumpkins", "candy","hello"]))

def h():
    global trick
    global treat
    return "treat"

trick = "midterm"
treat = "exam"
treat = h()

print(trick + " or " + treat)

def f(n):
    print(n)
n = 1
m = 2
f(m)

def f(L):
    L = [3]
L = [5]
f(L)
print(L[0])

"""def f():
    L[0] = 0
    L = [4, 5, 6]
L = [1, 2, 3]
f()
print(L)"""

L = [[1, 2], 3]
M = L[:]
M[0][1] = 5
M[1] = 5
print(L)

#Q5
def symtrix_list(L):
    return L == L[::-1]