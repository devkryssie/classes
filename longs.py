'''
fav_quote = input("Your favorite quote: ")
file_name = input("Enter file name : ")
extension = input("Enter file extension: ")

if extension == ".txt":
    with open(file_name, "a") as f:
        f.write(fav_quote )
    print("quote saved successfully", file_name + extension)
else:
    print("only .txt extensions are allowed")
 
save a quote file, and its file extension
check if the extension is equa to .txt then open a file name and append it as a file if it does not exist
a success messge if the extension is correct add the file name and the extension
else print an error message

int1,int2,int3 = 1,2,3

user = input("enter text: ")
print(user)
'''
a = 1
if type(a) == int:
    print(f"{a} is an integer")
else:
    print(f"{a} not an integer")
b = "is"
if type(b) == str:
    print(f"{b} is a str")
else:
    print(f"{b} not a str")
c = 5.5
if type(c) == float:
    print(f"{c} is a float")
else:
    print(f"{c} not a float")



