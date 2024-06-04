a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a > b & a > c:
    print(f"{a} is greater")
elif b > c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")
