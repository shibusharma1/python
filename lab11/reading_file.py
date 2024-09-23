# QN3
fp = open("hello.txt","r")
# lists = fp.readlines()
# for i in lists:
#     print(i,end="")
    
#Easy alternative
content = fp.read()
print(content)

# size of function
fp.tell()

fp.close()
