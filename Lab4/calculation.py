def calculation(x,y):

    add = x+y
    sub = x-y
    mul = x*y
    div = x/y
    mdiv = x % y
    
    return add,sub,mul,div,mdiv


a,s,m,d,mdiv = calculation(4,2)

print("Sum :",a,"\n"," Subtract :",s,"\n"," multiplication :",m,"\n"," Division :",d,"\n"," Modulas division :",mdiv)
