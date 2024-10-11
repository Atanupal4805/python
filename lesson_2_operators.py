# Write a Python program to demonstrate the use of arithmetic operators.
a=14
b=15
print('the sum is : ',a+b)
print('the sub is : ',a-b)
print('the div is : ',a/b)
print('the multi is : ',a*b)
print('the mod is : ',a%b)
print('the power is : ',a**b)


# write a Python program to demonstrate the use of assignment operators. 
a = 10

# Assignment operator: '='
b = a
print("After b = a, b =", b)

# Add and assign: '+='
a += 5  # Equivalent to: a = a + 5
print("After a += 5, a =", a)

# Subtract and assign: '-='
a -= 3  # Equivalent to: a = a - 3
print("After a -= 3, a =", a)

# Multiply and assign: '*='
a *= 2  # Equivalent to: a = a * 2
print("After a *= 2, a =", a)

# Divide and assign: '/='
a /= 4  # Equivalent to: a = a / 4
print("After a /= 4, a =", a)

# Modulus and assign: '%=' gives the remainder
a %= 3  # Equivalent to: a = a % 3
print("After a %= 3, a =", a)

# Exponent and assign: '**='
a **= 2  # Equivalent to: a = a ** 2
print("After a **= 2, a =", a)

# Floor division and assign: '//='   give result
a //= 2  # Equivalent to: a = a // 2
print("After a //= 2, a =", a)


# write a Python program to demonstrate the use of comparison operators.
a=12
b=12
print('a==b= ',a==b)
print('a!=b= ',a!=b)
print('a>b= ',a>b)
print('a<b= ',a<b)
print('a>=b ',a<=b)
print('a<=b',a<=b)


# Write a Python program to demonstrate the use of logical operators.
a='true'
b='false'
print('a and b =',a and b)
print('a or b =',a or b)
print('not a =',not a)


# Write a Python program to find the average of three numbers .
a=float(input('enter the value of a : '))
b=float(input('enter the value of b : '))
c=float(input('enter the value of c : '))
average=(a+b+c)/3
print(f'the average of the three numbers is {average}')


# Write a Python program to convert Celsius to Fahrenheit .
a=float(input('the celsius is : '))
fahrenheit=(a*9/5)+32
print(f'the calculated fahrenheit is {fahrenheit}')


#  Write a Python program to check if a number is even or odd.
a=float(input('enter a number : '))
if(a%2==0):{
    print(f'the numer {a} is even')
}
else:{
    print(f'the number {a} is odd')
}


# Write a Python program to check if a number is positive, negative, or zero.
a=float(input('enter a number : '))
if(a==0):{
    print(f'the number is zero')
}
elif(a>0):{
    print(f'the number is positive')
}
else:{
    print(f'the number is negative')
}


# Write a Python program to check if a year is a leap year.
a=float(input('enter a year :'))
if(a%4==0):{
    print(f'{a} is a leap year')
}
else:{
    print(f'{a} is a normal year')
}


#  Write a Python program to calculate simple interest.
a=float(input('enter the principal amount : '))
b=float(input('enter the interest rate you want to apply : '))
c=float(input('enter the time period : '))
simple_interest=(a*b*c)/100
print(f'the simple_interest is : {simple_interest} ')
