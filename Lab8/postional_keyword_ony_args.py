#Positional only Arguments
def pos_Only_Arguments(a,b,/):
    print("Value of a & b are",a,b)

pos_Only_Arguments(5,6)


#Keyword Only Arguments
def keyword_Only_Arguments(*,a,b):
    print("Value of a & b are",a,b)

keyword_Only_Arguments(b=5,a=6)