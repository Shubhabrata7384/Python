#In a game, bonus points for each level follow a Fibonacci pattern. Write a program to calculate the bonus for level N. Take level number as user input.
n = int(input("Enter the level number: "))

# First two Fibonacci numbers
a, b = 0, 1

if n == 1:
    print("Bonus for level", n, "=", a)
elif n == 2:
    print("Bonus for level", n, "=", b)
else:
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    print("Bonus for level", n, "=", b)
