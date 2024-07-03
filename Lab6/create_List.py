li = [1,3,5,7]
for i in li:
    print(i,end=" ")

print()

# anotherway of creating list
names = list()
n = int(input("Enter the number of students you want to add"))
for i in range(n):
    name = input("Enter the name of student:")
    names.append(name)
print("SN\t Name")
for id,name in enumerate(names,start=1):
    #enumerate():tracks the loop count
    print(id,"\t",name)
    
