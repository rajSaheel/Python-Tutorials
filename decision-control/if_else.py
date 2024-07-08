"""
In any language there are 4 major components available:
1. Data(data-type)
2. Decision-Control Structure/If-else
3. Iteration/Looping
4. Functions
5. Import/Export"""

# Write a program WAP to print whether it is a holiday

char = input("Enter the day: ")

days = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
check = char.lower()

if(check in days):
    if(check == "sunday"):
        print("Wohoo! It is a holiday.")
    else:
        print("Ooops! you have to go to work today.")
else:
    print("this day does not exist")