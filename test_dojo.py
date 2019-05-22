#!/usr/local/bin/python3

string = "This is the string with which we will be working."
string = string.lower()
print(string)

new_string = []
for char in range(0,len(string)-1):
    if char % 2 == 0:
        new_string.append(string[char].upper())
    else:
        new_string.append(string[char])

print("".join(new_string))
