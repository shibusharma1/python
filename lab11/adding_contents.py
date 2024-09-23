fp = open("hello.txt",'a')
fp.writelines("\nThis is line two\n")
fp.writelines("This is line 3")
fp.close()