#8. Write a Python program to perform following operation on given string input:
#a) Count Number of Vowel in given string
#b) Count Length of string (donot use len() )
#c) Reverse string
#d) Find and replace operation
#e) check whether string entered is a palindrome or not

s = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
for ch in s:
    if ch in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)


length = 0
for ch in s:
    length += 1
print("Length of string:", length)

rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)

find_char = input("Enter character/string to find: ")
replace_char = input("Enter character/string to replace with: ")
new_string = ""
i = 0

while i < length:
    if s[i:i+len(find_char)] == find_char:
        new_string += replace_char
        i += len(find_char)
    else:
        new_string += s[i]
        i += 1

print("String after replace:", new_string)

if s == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
