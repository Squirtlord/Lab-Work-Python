#let the temp in fahrenheit = x and celsius = y
y=int(input("Enter Temperature"))
for y in range (-100,100):
    x=(9*y+160)/5 
    if x==y:
         print(x)