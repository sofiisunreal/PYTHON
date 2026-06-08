# functions with return
def sum():
    num1=10
    num2=20
    ans=num1+num2
    print(f"The sum of {num1} and {num2} is: {ans}")

# call the function
sum()

# functions with parameters
def sum1(num1,num2):
    ans=num1+num2
    print(f"The sum of {num1} and {num2} is: {ans}")

# call the function
sum1(50,30)
sum1(250,400)

# functions with return
def sum2(num1,num2):
    ans=num1+num2
    return(ans)
print(sum2(60,30))
result=sum2(90,10)
print(result)

