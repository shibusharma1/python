sentence ="I am a good boy"
for x in sentence:
    print(x,end="") #end is a parameter of print which add "" at the end of the each word.By default print has \n which will place the word in new line each time.
print()
count=len(sentence)
for x in range(count):
    print(sentence[x],end="")

sentence1 = str.lower(sentence)
if "Good" in sentence1:
    print("\nGood exist in the sentence.")
else:
    print("\nGood doesnot  exist in the sentence.")

if "Bad" not in sentence1:
    print("\nBad doesnot exist in the sentence.")
else:
    print("\nBad exist in the sentence.")
