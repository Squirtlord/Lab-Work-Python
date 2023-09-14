y=int(input("enter any year "))
if y%400==0 and y%4==0:
    print(y,"is a leap year")
else:
    print(y,"is not a leap year")