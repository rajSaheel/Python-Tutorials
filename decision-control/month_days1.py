birth_month = int(input("Enter the birth month in number: "))

month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

if birth_month > 12 or birth_month < 1:
    print("Enter a valid number")
else:
    print(month_days[birth_month - 1])
