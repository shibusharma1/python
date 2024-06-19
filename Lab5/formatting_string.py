username = input("Enter your Name:")
sem = input("Enter your Sem:")
pgm = input("Enter your Program:")

#one way using f-string
msg= f"""
Hello {username},

We hope you are doing well.
We the students of {sem}
are going to organize a
{pgm} program on 2081/03/15.

we hope to see you there.

Thanking you
{sem} Students.
"""
print(msg)

#Alternative way using format() function
msg1= """
Hello {},

We hope you are doing well.
We the students of {}
are going to organize a
{} program on 2081/03/15.

we hope to see you there.

Thanking you
{} Students.
""".format(username,sem,pgm,sem)

print(msg1)
