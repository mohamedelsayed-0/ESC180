#Q3
def generate_hats(num_students):
    import random
    hats = []
    for i in range(num_students):
        if random.random() < 0.5:
            hats.append("W")
        else:
            hats.append("B")
    return hats

def count_white_hats(hats):
    count = 0
    for i in hats:
        if i == "W":
            count += 1
    return count


def make_guesses(hats):
    guesses = []
    n = len(hats)
    for i in range(n):
        hats_seen = 0
        for j in range(n):
            if i != j and hats[j] == "W":
                hats_seen += 1
    
        if hats_seen % 2 == 0:
            guesses.append("B")
        else:
            guesses.append("W")

    return guesses

def are_all_guesses_correct(hats, guesses):
    if hats == guesses:
        return True
    else:
        return False

#Q4
def gcd(n,m):
    greatest = 1
    for i in range(n,m+1):
        if m % i == 0 and n % i == 0:
            greatest = i
    return greatest


if __name__ == "__main__":
    num_students = 12
    hats = generate_hats(num_students)
    print("Hats: ", hats)
    guesses = make_guesses(hats)
    print("Guesses: ", guesses)
    if are_all_guesses_correct(hats, guesses):
        print("All guesses correct!")
    else:
        print("Not all guesses correct.")

    print(gcd(12,48))