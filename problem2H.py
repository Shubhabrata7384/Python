# 2. Write a Python function to convert Fahrenheit to Celsius.
def fahrenheit_to_celsius(f):
    return 5*(f-32)/9
n=int(input("Enter temperature in fahrenheit: "))
print(f"The temperature in celsius is : {fahrenheit_to_celsius(n)}")