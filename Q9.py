p=float(input("enter principle amount "))
t=float(input("enter time period for RD "))
r=7.1
SI=p*r*t/(100*12)
if t>6 and p>500:
    print(SI)
else:
    print("invalid inputs")