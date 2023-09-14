a=float(input("enter a side of the triangle "))
b=float(input("enter a side of the triangle "))
c=float(input("enter a side of the triangle "))
if a+b>c and b+c>a and c+a>b:
    print("A TRIANGLE IS FORMED")
else:
    print("A TRIANGLE IS NOT FORMED")