# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

year = int(input("Enter the year to detemine whether given year is leap year: "))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"Wooho! correct {year} is leap year")
elif year % 4 == 0 & year % 100 != 0:
    print(f"Wooho! correct {year} is leap year")
else:
    print(f"No {year} is not leap year")
