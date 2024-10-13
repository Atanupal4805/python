# Write a Python program to create a list of numbers.
number=input('enter some numbers: ')
list_of_numbers=[number]
print(f'the list of number is {list_of_numbers}')


# Write a Python program to find the sum of all elements in a list.
number=list(map(int,(input('enter some numbers: ').split())))

print(f'the list of number is: {number}')
total_sum=sum(number)
print(f'the sum is {total_sum}')


# Write a Python program to find the largest and smallest number in a list.
number=list(map(int,(input('enter some number with giving space in between them : ').split())))
print(f'the list of numbers is: {number}')
largest_number=max(number)
smallest_number=min(number)
print(f'the largest number on the list is : {largest_number} and the smallest number on the list is : {smallest_number}')


# Write a Python program to sort a list in ascending and descending order.
number=list(map(int,(input('enter some numbers with giving space after entering each number : ').split())))
print(f'the number list is {number}')

number.sort()
print(f'the ascending order of the list is :{number}')
number.sort(reverse=True)
print(f'the descending order of the list is :{number}')


# Write a Python program to remove duplicates from a list.
number=list(map(int,(input('enter some number with giving spaces after each number : ').split())))
remove_duplicates=list(set(number))
print(f'the list is :{remove_duplicates}')


# Write a Python program to check if an element exists in a list.
number=list(map(int,(input('enter some numbers with giving space after each number : ').split())))
print(f'the list of numbers is : {number}')
search_number=int(input('enter the number which you want to search : '))
found=False
for num in number:
    if num==search_number:
        found==True
        break

if found:
    print(f'the number {search_number} is present in the number list.')
else:
    print(f'the number {search_number} is present in the list.')


# Write a Python program to count occurrences of an element in a list.
number=list(map(int,(input('enter some number with giving space after each number: ').split())))
print(f' the list of number which you have entered is : {number}')
num=int(input('enter the number which you want to count its occurrences : '))

count=0
for c in number:
    if c==num:
        count+=1

print(f'the number  {num} appears {count} times in {number}')


# Write a Python program to merge two lists into one.
positive_number=list(map(int,(input('enter some positive number with giving space after each number : ').split())))
print(f'the positive numbers are : {positive_number}')
negative_number=list(map(int,(input('enter some negative number with giving space after each number : ').split())))
print(f'the negative numbers are : {negative_number}')

marge_list=list(set(positive_number + negative_number))
print(f'the marge list of all the numbers provided by the user : {marge_list}')


# Write a Python program to find the index of an element in a list.
number=list(map(int,(input('enter some number and give space after each number : ').split())))
print(f'the list of numbers are : {number}')

num=int(input('enter the number which you want to find index : '))
if num in number:
    index_of_number=number.index(num)
    print(f'the number {num} is present in the index of {index_of_number}')

else:
    print(f'the number {num} is not present on the list')


# Write a Python program to remove an element from a list.
number=list(map(int,(input('enter some number and give space after each number : ').split())))
print(f'the list of number are : {number}')
num=int(input('enter a number which you want to remove from the list : '))
if num in number:
    removed_number=number.remove(num)
    print(f'the number {num} is removed.So the new list is {number}')

else:
    print(f'the number {num} is not present on the predefined list.')






