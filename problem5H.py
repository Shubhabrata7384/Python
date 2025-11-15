# 5. Write a Python function to print the following pattern using recursion.
def pattern(n):
    if(n==0):
        return
    print("* " * n)
    pattern(n-1)
n=int(input("Enter number of rows: "))
pattern(n)