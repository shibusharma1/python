def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print(list[idx],end=" ")
    print_list(list,idx+1)\

fruits = ["mango","litchi","apple","banana"]
print_list(fruits)