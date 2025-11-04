# Program to greet all the person names stored in a list which start with 's'
l=["harry","shubhabrata","rohit","anurag","subham"]

for name in l:
    if(name.startswith("s")):
        print(f"hello {name}")