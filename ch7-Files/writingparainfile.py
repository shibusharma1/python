# Hi everyone
# we are learning File I/O
# using python
# I like programming in python

with open("sample.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using python\nI like programming in python")
    f.close()
    print("Content Written into file successfully.")