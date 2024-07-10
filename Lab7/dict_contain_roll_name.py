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






# l) clear the items from students
students = {1:"ram"} 
print(students)
students.clear() #clears all the items from the dictionary
print(students)
students=None #dictionary lai none ma convert grxa more we need to research for it

print(students)