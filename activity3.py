#input a word
text= str(input("Enter a string: "))

# Reverse string
# using step value as -1 to iterate in reverse
revText= text[::-1]
text=revText

print(f"Reverse of Given String is: {text}" )