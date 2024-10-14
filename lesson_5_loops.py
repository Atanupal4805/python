# Write a Python program to print numbers from 1 to 10.
i=list(range(1,11))
for num in i:
    print(f'numbers: {num}')


# Write a Python program to print the multiplication table of a given number.
number=int(input('enter a number : '))
for i in range(1,11):
    print(f'the multiplication table of {number} x {i} is : {number*i} ')


# Write a Python program to find the sum of all numbers from 1 to 100.
i=list(range(1,101))
total_sum=sum(i)
print(f'the sum is : {total_sum}')


# Write a Python program to print the first 10 Fibonacci numbers.
def fab(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n < 1:
        print('Please enter a positive number to get a Fibonacci series')
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(list(map(int,c)))
n = int(input('Enter a number to get a Fibonacci series: '))
fab(n)


# Write a Python program to print all even numbers from 1 to 100.
for i in range(1,101):
    if i%2==0:
        print(i)


# Write a Python program to find the greatest common divisor (GCD) of two numbers.
a=int(input('enter a number : '))
b=int(input('enter another number: '))
if a>b:
    min=b
else:
    min=a
for i in range(1,min+1):
    if a%i==0 and b%i==0 :
        HCF=i
print(f'the GCD/HCF of {a} and {b} is : {HCF}')


# Write a Python program to find the least common multiple (LCM) of two numbers.
a=int(input('enter a number: '))
b=int(input('enter another number: '))

maxNum=max(a,b)

while(True):
    if maxNum%a==0 and maxNum%b==0:
        break
    maxNum=maxNum+1
print(f'the LCM of {a} and {b} is {maxNum}')


# Write a Python program to check if a number is prime.
a=int(input('enter a number: '))
if a<2:
    print(f'{a} is not a prime number.')
else:
    is_prime=True
    for i in range(2,a):
        if a%i==0:
            is_prime=False
            break

if is_prime:
    print(f'{a} is a prime number.')
else:
    print(f'{a} is not a prime number.')


# Write a Python program to print all prime numbers between 1 and 100.

for num in range(2,101):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end='\n')




