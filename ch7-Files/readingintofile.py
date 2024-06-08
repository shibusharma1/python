f=open("demo.txt","r")
content = f.read()
print(content)
print(type(content))
#it will return the data type str
f.close()