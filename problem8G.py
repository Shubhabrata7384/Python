# Program to print the multiplication table of a given number in reverse order
n=int(input("enter a number:"))

for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")
