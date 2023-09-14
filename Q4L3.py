X=int(input("Enter a three digit number "))
first_number=round(X/100)
print(first_number)
a=int(X-(first_number*100))
second_number=round(a/10)
print(second_number)
third_number=X%10
print(third_number)