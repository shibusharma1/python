#Create a recursive function
def fact(n):
    if(n == 0):
        return 1
    else:
        return n*fact(n-1)
    
n = int(input("Enter the number to find Factorial:"))
result = fact(n)
print(f"The factorial of {n} is {result}")