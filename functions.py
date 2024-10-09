'''#  Write a Python function to find the maximum of three numbers.
def find_max():
    a=int(input('enter the 1st number: '))
    b=int(input('enter the 2nd number: '))
    c=int(input('enter the 3rd number: '))
    if a>b and a>c:
        print(f'{a} is the greatest among all the three numbers .')
    elif b>a and b>c:
        print(f'{b} is the greatest among all the three numbers .')
    else:
        print(f'{c} is the greatest among all the three numbers .')
find_max()


# Write a Python function to calculate the factorial of a number.
def factorial():
    a = int(input('Enter a number: '))
    
    fact=1
    
    # Calculate factorial
    for i in range(1, a + 1):
        fact *= i  # Multiply fact by i (1, 2, ..., a)
    print(f'The factorial of {a} is: {fact}')

factorial()


# Write a Python function to check if a number is prime.
def find_prime():
    a=int(input('enter a number to check it is prime or not : '))
    if a<2:
        print(f'the number {a} is not a prime number. ')
        return
    else:
        is_prime=True
        for i in range(2,a):
            if a%i==0:
                is_prime=False
                break
                
    if is_prime:
        print(f'the number {a} is a prime number.')
    else:
        print(f'the number {a} is not a prime number.')
find_prime()


# Write a Python function to reverse a string.
def reversed_string():
    a=input('enter a string: ')
    reversed=a[::-1]
    print(f'the reversed string is : {reversed}')
reversed_string()


#  Write a Python function to find the GCD of two numbers.
def find_gcd():
    a=int(input('enter a number: '))
    b=int(input('enter another number: '))
    if a>b:
        min=b
    else:
        min=a
        for i in range(1,min+1):
            if a%i==0 and b%i==0:
                GCD=i
        print(f'the gcd/hcf of the two numbers is {GCD}')
find_gcd()


# Write a Python function to find the LCM of two numbers.
def find_lcm():
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
    
    lcm= max(a, b)  
    while True:
        if lcm % a == 0 and lcm % b == 0:
            break  # LCM 
        lcm += 1 
    
    print(f'The LCM of {a} and {b} is {lcm}')

find_lcm() 


# Write a Python function to count the vowels in a string .
def find_vowels():
    string=input('enter a string: ').lower()
    vowels=['a','e','i','o','u']
    found_vowels=[]
    for char in string:
        if char in vowels:
            found_vowels.append(char)
    if found_vowels:
        print(f'the string have vowels: {set(found_vowels)}. ')
    else:
        print(f'the string has no vowels in it.')
find_vowels()


# Write a Python function to find the sum of digits of a number.
def find_sum():
    number=input('enter a number: ')
    total_sum=0
    for digit in number:
        total_sum += int(digit)
    print(f'the sum of digits is : {total_sum}')
find_sum()


# Write a Python function to check if a number is a palindrome.
def find_palindrome():
    a=input('enter a number: ')
    reversed=a[::-1]
    print(f'the reversed number is : {reversed}')
    if reversed==a:
        print(f'the number {a} is a palindrome .')
    else:
        print(f'the number {a} is not palindrome .')
find_palindrome()'''


# Write a Python function to check if a string is an anagram of another string.
def find_anagram():
    a=input('enter a string : ').replace(" ","").lower()
    b=input('enter another string : ').replace(" ","").lower()
    if sorted(a)==sorted(b) :
        print(f'the string " b" is anagram of the string "a" .')
    else:
        print(f'the string "b" is not an anagram of the string "a" .')
find_anagram()