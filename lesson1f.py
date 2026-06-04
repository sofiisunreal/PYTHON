# dictionary  key value pairs
# we use curly braces 
# we acess items using the key  

student={
     "name":"John",
     "age":25,
     "course":"software",
     "languages":['python','tailwindcss','html']
}

print(student)

# accesing items 
print(student["name"])
print(student["age"])
print(student["course"])

# acess tailwindcss
print(student["languages"][1])

# add item 
student["email"]="std@gmail.com"
print(student)

# update 
student["age"]=30
print(student)

print(student.keys())
print(student.items())
print(student.values())