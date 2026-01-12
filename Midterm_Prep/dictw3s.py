thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 1965
}
print(thisdict)
print(len(thisdict))

thisdict2 = dict(name = "John", age = 36, country = "Norway")
print(thisdict2)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

