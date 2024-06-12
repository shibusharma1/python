
# ERROR not running code
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("sample.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                # print(line_no)
                return line_no
            # print(line_no)
            line_no += 1
        return -1
print(check_for_line())