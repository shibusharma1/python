with open("sample.txt","r") as f:
    data=f.read()
    new_data = data.replace("python","web II")
    print(new_data)
    f.close()

with open("sample.txt","w") as f:
    f.write(new_data)
