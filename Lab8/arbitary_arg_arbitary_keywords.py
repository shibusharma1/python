#WAP to show the use of Arbitary Arguments(*args) and Arbitary Keyword arguments(**arg)

#Arbitary Arguments Function
def arbitary_args(*args):
    for val in args:
        print(val)


#calling the Arbitary Arguments Function  
arbitary_args("Ram","Brt")
 
 
 
#Arbitary Keyword arg Functions   
def arbitary_keyword_args(**args):
    for key,val in args.items():
        print(key,"=>",val)


#calling the Arbitary Keyword arg Functions
arbitary_keyword_args(name="Ram",Address="Brt")
 