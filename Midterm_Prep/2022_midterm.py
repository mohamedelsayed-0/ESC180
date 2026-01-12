#Q1
def get_perfect_squares(n):
    squares = [0]
    for i in range(1,n+1):
        if (i**0.5).is_integer():
            squares.append(i)
    return squares
print(get_perfect_squares(36))

#Q2A
def prod(L):
    total = 1
    for i in L:
        total *= i
    return total
print(prod([2,3,4]))

#Q2B
def duplicates(list0):
    for i in range(0, len(list0) - 1):
        if list0[i] == list0[i+1]:
            return True
    return False

#Q3
def order():
    number = 0
    while True:
        x = input("What is your order? ").lower()
        if x != "pumpkin spice lover":
            number += 1
        else:
            break
    return number
    print(number)

#Q4
def matrix_sum(A,B):
    if len(A) != len(B):
        return "ERROR"
    sums = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        sums.append(row)
    return sums

#Q5
halloween_haul = {
    "house1": {
        "Annie": ["snickers", "mars"],
        "Johnny": ["snickers"]
    },
    "house2": {
        "Annie": ["coffee break", "mars"],
        "Jackie": ["coffee break"]
    }
}

def luckiest_kid(halloween_haul):
    seen = set()
    luckiest_kid = None
    count = 0
    max_count = 0
    for i in halloween_haul:
        for j in halloween_haul[i]:
            if i not in seen:
                count += 1
                if count > max_count:
                    max_count = count
                    luckiest_kid = i

#Q6
pi_digits = "3141592653"
index = 0
def next_digit_pi():
    global index
    if index < len(pi_digits):
        index += 1
        print(pi_digits[index])
    else:
        print("ERROR")
    
#Q7


    



    
    








def counting(n):
    n = abs(n)
    count = 0
    while n >0:
        n //= 10
        count+=1
    return count

print(counting(-300000000000000))





