# list - a collection of ordered items
# we use square brackets[]
# we use indexes to access items in alist 
# we use from index 0 

farmers=["John","Mary","Peter","Jane","Samuel"]
print(farmers)
print(type(farmers))

# acessing indexes 
print(farmers[0])
print(farmers[2])

# negative indexing 
print(farmers[-1])
print(farmers[-2])

# slicing
print(farmers[1:4])

print(farmers[2:])

print(farmers[:4])

# length 
print(len(farmers))

# if exists 
print("John" in farmers)
print("Ann" in farmers)

# list methods
# add
farmers.append("David")
print(farmers)

farmers.insert(1,"Grace")
print(farmers)

# remove
farmers.remove("Mary")
print(farmers)
farmers.pop(0)
print(farmers)

# arrange
farmers.sort()
print(farmers)

farmers.reverse()
print(farmers)


