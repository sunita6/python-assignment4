print("program to extract substring\n")
 
string=input("enter a sentence of ur choice:\n").lower()
search_letter=input("\nenter the search letter:").lower() 
length=len(string)
index=0
if length>0:
    if search_letter in string:
       count=string.count(search_letter)
       index=string.index(search_letter)
       print(f"\n substring count:{count}\n")
       print(f"length={length}\n")
       print(f"index of the substring:{index}\n")
    else:
       print("enter a valid search letter ?\n")


#output
program to extract substring

enter a sentence of ur choice:
what we think we become;we are Python programmer!!

enter the search letter:we

 substring count:3

length=50

index of the substring:5





