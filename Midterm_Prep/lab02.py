"""def my_sqrt(x):
    sqr = x**.5
    return sqr

def my_print_square(x):
    sqr = x**.5
    print(sqr)

if __name__ == "__main__":
    res = my_sqrt(25) 
    print(res)
    my_print_square(25)"""



#Q4
value = 0
def display_current_value():
    global value
    print(value)

def add(to_add):
    global value
    if type(to_add) == int:
        value += to_add
    else:
        print("Wrong value type")

def mult(to_mult):
    global value
    if type(to_mult) == int:
        value *= to_mult
    else:
        print("Wrong Value Type")

def div(to_div):
    global value
    if type(to_div) == int:
        value = (value / to_div)
    elif to_div == 0:
        print("Error, division by 0 is not possible")
    else:
        print("Wrong Value Type")

if __name__ == "__main__":
    print("Welcome to the calculator program.\nCurrent Value: 0")
    add(5)
    display_current_value()
    mult(5)
    display_current_value()
    div(5)
    display_current_value()

# memory recall not on test, ignore
