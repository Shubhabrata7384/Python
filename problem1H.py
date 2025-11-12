# 1. Write a Python function to find the greatest of three numbers.
def greatest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(greatest(23,43,33))
print("thanks for using the greatest function")