my_string= "Hello world"

print("-="*10)

print(f"number of characters in a string: {len(my_string)}") # counts the number of characters in a string
print(f"index of w in the string: {my_string.index('w')}") #returns index of a character in a string
print(f"To upper: {my_string.upper()}")
print(my_string.replace("o","a"))

name=input("Enter your name: ")
first_three_chars= name[:3]
no_o_chars= len(name)

#comparison operators

x= 44
y= 55

print(x==y)