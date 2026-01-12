#Q1A
def rate_costume(costume):
    if costume == "ghost" or costume == "zombie" or costume == "skeleton":
        return "Spooky!"
    else:
        return "Fun!"

#Q1B
def candy_pieces(num_pieces):
    if num_pieces < 20:
        return "Try more houses!"
    elif num_pieces >= 20 and num_pieces <= 49:
        return "Not Bad!"
    elif num_pieces >= 50:
        return "Great Haul!"

#Q1C
def below_avg(L):
    result = []
    avg = 0
    for i in L:
        avg += i
    avg = avg / (len(L))
    for i in L:
        if i < avg:
            result.append(i)
    return result

#Q2
count = int(input("How many times to repeat: "))
while count > 0:
    print("Trick or Treat!")
    count += -1

#Q3
def is_popular(faves, activity):
    count = 0
    for key in faves:
        if faves[key] == activity:
            count +=1
    if count > 1:
        return True
    else:
        return False
    
#Q4
def dot_product(v1,v2):
    for i in len(v1):
        for j in v2:
            result += (v1[i] * v2[j])
    return result

#Q5
def simulate_journey():
    result = 0
    state = "WALK"
    command = input("Enter a command ")
    while command != "END":
        new_command = input("Enter a command")
        if new_command == "WALK":
            state = "WALK"
            command = new_command
        if new_command == "RUN":
            state = "RUN"
            command = new_command
        if type(new_command) == int and state == "RUN":
            result += 6 * new_command
        if type(new_command) == int and state == "WALK":
            result += 3 * new_command
        if new_command == "END":
            return result
            