# Write a Python program to concatenate two strings.
print(f'Hi','how are you all today')
print(f'everyone should play football ' + 'because football is a great game.')


# Write a Python program to find the length of a string.
my_string='welcome to the hell.'
size=len(my_string)
print(f'good morning everyone .the length of my string is {size}')


# Write a Python program to count the occurrences of a character in a string.
my_string=input('enter a string: ')
char=input('enter the character : ')

count=0
for c in my_string:
    if c==char:
        count+=1

print(f'the character {char} appears {count} times in {my_string}')


# Write a Python program to check if a string is a palindrome.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
string=input('enter a string: ')
string=string.lower()
reversed_string = string[::-1]


if string==reversed_string:
    print(f'the string {string} is a palindrome.')

else:
    print(f'the string {string} is not a palindrome.')


# Write a Python program to convert a string to uppercase.
string=input('enter a string : ')
string=string.upper()
print(f'the string is converted to {string}') 


# Write a Python program to replace all occurrences of a substring in a string.
main_string=input('enter a string: ')
old_substring=input('enter the substring to replace: ')
new_substring=input('the new substring is : ')

modified_string=main_string.replace(old_substring,new_substring)

print(f'the modified string is : {modified_string}') 


# Write a Python program to find the first and last character of a string.
string=input('enter a string: ')
first_word=string.split()[0]
last_word=string.split()[-1]

print(f'the first word of the string is : {first_word} and the last word is : {last_word}')


# Write a Python program to reverse a string.
string=input('enter a string: ')
reversed_string=string[::-1]
print(f' the reversed string is : {reversed_string}')


# Write a Python program to split a string into a list of words.
string=input('enter a string : ')
word_list=string.split()
print(f'{word_list}')


# Write a Python program to remove whitespace from the beginning and end of a string.
string=input('enter a string: ')
trimmed_string=string.strip()
print(f'the string without the spaces is {trimmed_string}')







