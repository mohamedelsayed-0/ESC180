mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

L = [1, 2, 3, 2, 4, 2]
value = 2

indexes = [i for i, x in enumerate(L) if x == value]
print(indexes)  


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
