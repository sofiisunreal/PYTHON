# if..elif..else- allows more than one condition 
# the else block gets executed only when all the conditions have failed/false 

# if condition1:
     # block of code 
# elif condition2:
     # block of code 
# elif condition3:
     # block of code 
# else: 
     # default block of code 


litres=30
if litres>=100:
     print("Premium Farmer")
elif litres>=50:
     print("Regular Farmer")
else:
     print("Small scale farmer")

# check if number is zero,even or odd 
number=int(input("Enter a number: "))
if number>0:
     print("The number is positive")
elif number<0:
     print("The number is negative")
else:
     print("The number is zero")