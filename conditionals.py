'''# Write a Python program to check if a number is divisible by 5.
a=int(input('enter a number: '))
if a%5==0:
    print(f'{a} is divisible by 5 ')
else:
    print(f'{a} is not divisible by 5')


# Write a Python program to check if a number is divisible by 3 and 7.
a=int(input('enter a number : '))
if a%3==0 and a%7==0:
    print(f'{a} is divisible bt both 3 and 7 .')
else:
    print(f'{a} is not divisible by 3 and 7 .')


# Write a Python program to find the largest of three numbers.
a=int(input('enter a number: '))
b=int(input('enter a number: '))
c=int(input('enter a number: '))

if a>b and a>c:
    max=a
    print(f'{max} is the greatest number in between the three number {a},{b},{c} .')
elif b>a and b>c:
    max=b
    print(f'{max} is the greatest number in between the three number {a},{b},{c} .')
else:
    max=c
    print(f'{max} is the greatest number in between the three number {a},{b},{c} .')


# Write a Python program to check if a number is a perfect square.
a=int(input('enter a number: '))
is_perfect_square=False
for i in range(100000):
    if a==i*i:
        print(f'{a} is a perfect square of {i}')
        is_perfect_square=True
        break
if not is_perfect_square:
    print(f'{a} is not a perfect square.')


# Write a Python program to check if a string is empty.
a=input('enter a string: ')
if a=="":
    print(f'the string is empty.')
else:
    print(f'the string is not empty : {a}. ')


# Write a Python program to check if a list is empty.
a=list(map(int,(input('enter sum numbers by giving spaces after each number: ').split())))
if not a:
    print(f'the list is empty.')
else:
    print(f'the list is not empty : {a}.')


# Write a Python program to determine if a year is a leap year using logical operators.
a=int(input('enter a year : '))
if a%4==0 and a%400!=0:
    print(f'the year {a} is a leap year.')
else:
    print(f'the year {a} is not a leap year.')


# Write a Python program to implement a simple calculator using if-else conditions.
a=int(input('enter a number: '))
b=int(input('enter another number: '))
operator=input('enter the operator which you want to use (+,-,*,/,%): ')
if operator=='+':
    sum=a+b
    print(f'the sum is: {sum}')
elif operator=='-':
    sub=a-b
    print(f'the sub is: {sub}')
elif operator=='*':
    multi=a*b
    print(f'the multiply of two number is: {multi}')
elif operator=='/':
    div=a/b
    print(f'the division is: {div}')
elif operator=='%':
    mod=a%b
    print(f'the mod is: {mod}')
else:
    print(f'please enter a valid operator : {operator}')


# Write a Python program to check if a triangle is valid using sides of a triangle.
a=int(input('enter a base of a triangle: '))
b=int(input('enter the hight  of a triangle: '))
c=int(input('enter the hypotenuse of a triangle: '))
if c>a+b:
    print(f'the triangle is valid.')
else:
    print(f'the triangle is not valid.')'''


# Write a Python program to find the grade of a student based on marks.
a=int(input('enter the marks obtain by the student in the board exam : '))
if a>90:
    print(f'the student got "A" in the exam')
elif a>80:
    print(f'the student got "B" in the exam') 
elif a>70:
    print(f'the student got "C" in the exam') 
elif a>60:
    print(f'the student got "D" in the exam')  
elif a>50:
    print(f'the student got "E" in the exam')
elif a>40:
    print(f'the student got "F" in the exam') 
else:
    print(f'the student is fail in the board exam .')    


