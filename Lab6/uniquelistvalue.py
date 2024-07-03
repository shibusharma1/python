Students=['Ayusha',"Amish","Amogh","Babita","Babita"]

li = set(Students)

print(list(li))

#using membership operator

newli=list()

for student in Students:
    if student not in newli:
        newli.append(student)

print(newli)