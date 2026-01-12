#Q1

def print_halloween(month,day):
    if month == "oct" and day == 31:
        print("Happy Haloween")
    else:
        print("Not Haloween")

#Q2
def sum_even_squares(L):
    total = 0
    for i in L:
        if i % 2 == 0:
            total += i**2
    return total

#Q3
seen = set()
def is_sorted(L):
    if sorted(L) != sorted(seen(L)):
        return False
    elif sorted(L) == L:
        return True
    elif sorted(L, reverse = True) == L:
        return True
    else:
        return False



#Q4
def print_trick_or_treat_for(name):
    if name == "cluett" or "stangeby":
        print("trick")
    elif name == "davis":
        print("treat")
    else:
        print("no candy for you")

#Q5
def count_occurrences(n, target):
    total = 0
    for target in n:
        total += 1
    return total

#Q6
def most_frequent_fave(faves):
    favorite = None
    max_count = 0
    seen = set()
    count = 0
    for i in faves:
        if i not in seen:
            count += faves.count(i)
            if count > max_count:
                max_count = count
                favorite = i
    return favorite
print(most_frequent_fave(["candy", "costumes", "midterms", "candy"]))



