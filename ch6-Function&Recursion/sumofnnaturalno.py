def sum(n):
    if(n == 0):
        return 
    return n + sum(n-1)
sum1 = sum(10)
print("The sum of first natural numeber :-",sum1)