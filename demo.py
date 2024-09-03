'''a = int(input("Enter first number:\t"))
b = int(input("Enter second number:\t"))
c = a+b
print("the result is",c)

firstname = input("Enter the first name:\t")
lastname = input("Enter the last name:\t")
username= firstname + lastname
print("email is",username+"@gmail.com")'''

principle= int(input("Enter the principle amount to calculate the interest:\t"))
years= int(input("Enter the tenure in months:\t"))
rate_of_interest = float(input("Enter the interest rate:\t"))

interest = float((principle * float(years/12) * rate_of_interest)/100)

print(f"The interest on principle amount ${principle} for tenure of {years} with rate of interest {rate_of_interest} is $"+str(interest))