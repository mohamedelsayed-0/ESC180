#Q1
def compare(a,b):
    if a > b:
        return "larger"
    elif a < b:
        return "smaller"
    elif a == b:
        return "equal"

print(compare(6,6))

#Q2
for i in range(180,1801):
    if i != 1000:
        print(i)

#Q3
def even_numbers(a,b):
    result = []
    for i in range(a,b+1):
        if i % 2 == 0:
            result.append(i)
    return result

print(even_numbers(3,10))

#Q4
def not_halloween(L):
    count = 0
    for i in range(len(L)):
        if L[i] != "pumpkin" and L[i] != "ghost" and L[i] != "candy":
            count += 1
    return count

print(not_halloween(["cat", "candy"]))

#Q5
def favorite_candy(faves, c):
    count = 0
    for kid in faves:
        if faves[kid] == c:
            count += 1
    return count

print(favorite_candy({"Alice": "Mars"}, "Mars"))

#Q6
def fave_candies(faves, c):
    result = []
    for key in faves:
        if faves[key] == c:
            result.append(key)
    return result

#Q7
def zeros(x):
    index = 0
    while x < 1:
        index += 1
        x *= 10
    return index

print(zeros(0.12))
int(0.01)