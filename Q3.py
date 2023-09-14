x=int(input("enter any numb x "))
y=int(input("enter any numb y "))
if x<0 and y<0:
    print("not valid,enter a positive value")
elif y%x==0:
    print("y is divisible by x")
else:
    print("y is not divisible by x")