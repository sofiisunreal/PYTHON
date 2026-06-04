# tuple- is a collection of items but its immutable
# meaning you cannot add, remove or update an item in a tuple 
# we access items in the same way a list using indexes
# we start from index 0 
# we use parenthesis () to denote a tuple 

agricultural_counties=("Nakuru","Nyandarua","Kericho","Meru","Muranga","Uasin Gishu")

print(agricultural_counties)
print(type(agricultural_counties))

# access kericho 
print(agricultural_counties[2])

# access nyandarua to muranga 
print(agricultural_counties[1:5])

# acess meru to uasin gishu 
print(agricultural_counties[3:])

# nakuru to meru 
print(agricultural_counties[:3])