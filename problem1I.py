#An online store records the prices of items in an array. Write a program to sort the prices from lowest to highest. Display the sorted output.
n = int(input("Enter number of items: "))

prices = []
for i in range(n):
    price = float(input("Enter price: "))
    prices.append(price)

prices.sort()

print("Sorted prices (low to high):", prices)
