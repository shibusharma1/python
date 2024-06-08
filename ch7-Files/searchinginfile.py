word = "learning"
with open("sample.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Word Found")
    else:
        print("Word not Found")