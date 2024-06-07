#sum of first n terms 
sum = 0
n = int(input("Enter the number:"))
for i in range(n+1):
    sum+=i
print("Total sum = ",sum)