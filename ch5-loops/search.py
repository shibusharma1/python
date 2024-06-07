nums = [1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter the number to be search:-"))
idx = 0
for el in nums:
    if (el ==x):
        print("Number found at idx:-",idx)
    idx+=1

