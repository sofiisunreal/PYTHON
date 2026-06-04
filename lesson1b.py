#strings - sequence of characters of alphanumeric characters enclosed in""/''
message="Welcome to Django"
print(message)

# length 
print(len(message))

# convert to uppercase 
print(message.upper())

# lowercase 
print(message.lower())

# capitalize 
print(message.title())

# replace 
print(message.replace("Django", "Python"))

# accessing characters using indexes
print(message[0])

# slicing 
print(message[:7])

# concatenation 
greeting="Good"
time="Morning"
print(greeting+ " "+time)