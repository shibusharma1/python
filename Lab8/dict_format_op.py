# Q.N7. A function which accepts dictionary and print like "Hello Ram,Welcomee to HDC"
def display_in_format(student_detail):
    for key,value in student_detail.items():
        print(f"Hello {value['name']},Welcome to {value['col']}")
        
    
    print("Alternative way")
   
    for key,value in student_detail.items():
        name = value.get('name')
        col = value.get('col')
        print(f"{name}, {col}")
        
        
        
student_detail={
    1:{
        "name":"Ram",
        "col":"HDC"
        
    },
    2:{
        "name":"Shyam",
        "col":"ADC"   
    }
}

display_in_format(student_detail)


