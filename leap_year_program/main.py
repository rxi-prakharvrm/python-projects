year = int(input("Enter a year: "))

# Ternary in python
print("Leap year.") if ((year%4==0 and year%100!=0) or year%400==0) else print("Not leap year.")