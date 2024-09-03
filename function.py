'''
# function to remove duplicates in list
def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list

Ids = [1,2,3,4,5,5,6,3,5,7,8,1,9,3,5]
filtered_list = remove_duplicates(Ids)
print(f"filtered list is {filtered_list}")

#TO check if the word is palindrome
word = input("Enter the word to check :\t")
l = len(word)
palindrome_flag = True
for i in range(l):
    if word[i] != word[l-1-i]:
        palindrome_flag = False
        break
    else:
        palindrome_flag = True
if palindrome_flag:
    print("Word is palindrome")
else:
    print("Word is not palindrome")


# Function to check if the word is palindrome
def palindrome_check(word):
    palindrome_flag = True
    for i in range(len(word)):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

print(palindrome_check("python"))

#Function for EMI calculator
def emi_calculator(principal,rate,time):
    r = rate/12/100
    amount = (principal * r * (1+r)**time) / ((1+r)**time - 1)
    return amount
amount_to_be_paid = emi_calculator(5000000,5,24)
print(amount_to_be_paid)

# Function to calculate the factorial of the number
def fact(number):
    if number == 1:
        return 1
    else:
        return number * fact(number-1)

print(fact(5))


#Function with variable length argument
def add(*args):
    sum = 0
    for arg in args:
        sum = sum + arg
    return sum
print(add(1,2,3,4,5,6,7,8,9))

# Function for keyword variable length argument

def add(**kwargs):
    for key,value in kwargs.items():
        print(key + ":" + value)
add(name= "iphone", price= "700")
add(name= "ipad" , price= "300", description = "This is Ipad")

# Decorator in Python
def div_decorator(func):
    def wrapper(a,b):
        if a < b:
            a,b=b,a
        return func(a,b)
    return div

@decorator
def div(a,b):
    print(a/b)

div(2,4)

#Decorator with function example
def summer_discount_decorator(func):
    def wrapper(price):
        func(price)
        return func(price/2)
    return wrapper

@summer_discount_decorator
def total(price):
    return price
print(total(100))

'''



