# Q1. Create a dictionary which contains roll no and name of students
students={
    1 : "Ram",
    2 : "Shyam",
    3 : "Hari"
}
# Print the data in pattern : Hello ram your roll no is 1
for idx,name in students.items():
    print(f"Hello {name} your roll no is {idx}.")
    
# print all the keys
print(students.keys())

# print all the values available
print(students.values())

# check the roll no 2243 exist or non
key=students.keys()
if(2243 in key):
    print("2243 exist in the students")
else:
    print("2243 doesnot exist in the students")
    
#add student sangam with roll 20
# update() le data xaina vane add grxa else modify/change/replace grxa
students.update({20:"sanam"})

# change the name of student roll 20 to sanam
students.update({20:"sangam"})
print(students)







#delete roll no 20
del students[20]
print(students)


#copy dict and create new dict called new_students
print("List Copy")
new_students={}
new_students=students.copy()
print(new_students)

#adding new student to new_students
new_students.update({209:"Ravi"})
print("Students:")
print(students)

print()
print("New Students:")
print(new_students)
print()

#remove the recently added student
print("Pop Items")
print(students.popitem())
print()

# create a new_dict from Students and add a student in it and the same should be reflected in students
new_dict = students
new_dict.update({204:"Shyam"})
# New Dict
print("New Dictionary:")
print(new_dict)
#Old Students
print("Students")
print(students)


# l) clear the items from students
students = {1:"ram"} 
print(students)
students.clear() #clears all the items from the dictionary
print(students)
students=None #dictionary lai none ma convert grxa more we need to research for it

print(students)