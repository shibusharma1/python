def sum_of_items(list_of_colletion):
    s=0
    for val in list_of_colletion:
        s+=val
    return s

list_of_colletion=[3,6,7]
result = sum_of_items(list_of_colletion)
print(result)

#Alternative method
def sum_of_items(list_of_colletion):
    return sum(list_of_colletion)

list_of_colletion=[6,7]
result = sum_of_items(list_of_colletion)
print(result)
