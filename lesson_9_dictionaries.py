# Write a Python program to create a dictionary from two lists.
keys=['name','enroll','class','branch','sem']
values=['zoro',12,'A1','CSE','RGPV']

my_dict=dict(zip(keys,values))
print(f'the dictionary is created from two list is : {my_dict}')


# Write a Python program to add a key-value pair to a dictionary.
my_dict['profession']='engineer'
print(f'the modified dictionary is : {my_dict}')


# Write a Python program to remove a key from a dictionary.
del my_dict['sem']
print(f'the modified dictionary is : {my_dict}')


# Write a Python program to check if a key exists in a dictionary.
for keys in my_dict:
    if keys=="age":
        print(f'the key {keys} is present:')
        break
else:
    print(f'the key is not present')


# Write a Python program to get all keys and values from a dictionary.
for keys,values in my_dict.items():
    print(f'{keys}:{values}')


# Write a Python program to merge two dictionaries.
keys=['age','city','lover','present',]
values=[20,'bhopal','pandey','yes']

my_dict_2=dict(zip(keys,values))

my_dict.update(my_dict_2)
print(f'the merge dictionary is : {my_dict}')


# Write a Python program to sort a dictionary by key.
keys=['apple','orange','mango','banana','guava']
values=[10,4,21,31,2]
fruit_list=dict(zip(keys,values))
sorted_fruit_list=dict(sorted(fruit_list.items(),key=lambda item:item[0]))
print(f'the sorted dictionary by key is :{sorted_fruit_list}')


# Write a Python program to sort a dictionary by value.
sorted_fruit_list=dict(sorted(fruit_list.items(),key=lambda item:item[1]))
print(f'the sorted dictionary by value is :{sorted_fruit_list}')


# Write a Python program to find the maximum and minimum values in a dictionary.
max_value=max(sorted_fruit_list.values())
print(f'the max value is {max_value}')

min_value=min(sorted_fruit_list.values())
print(f'the min value is {min_value}')


# Write a Python program to count the frequency of elements in a list using a dictionary.
elements=['a','b','a','x','x','x','a','d','d','d','v','f','z','d']
frequency={}
for char in elements:
    if char in frequency:
        frequency [char]+=1
    else:
        frequency [char]=1
sorted_frequency=dict(sorted(frequency.items(),key=lambda item:item[0]))
print(f'the frequency is {sorted_frequency}')

