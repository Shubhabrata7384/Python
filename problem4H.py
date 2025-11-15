# 4. Write a Python function to sum all the numbers in a list.
def sum(n):
    if (n==1):
        return 1
    return sum(n-1)+n
n=int(input("Enter a number: "))
print(f"the sum is : {sum(n)}")