# In programming language we can also check nested condition

# To find the order no among three numbers

number1=int(input("Enter first number:- "))
number2=int(input("Enter second number:- "))
number3=int(input("Enter third number:- "))

# no1: 10009
# no2: 20600
# no3: 4000

if(number1>number2 ):
    if(number1>number3):
        if(number2>number3):
            print(number1," ",number2," ",number3)
        else:
            print(number1," ",number3," ",number2)
    else:
        print(number3," ",number1, " ",number2)   
else:
    if(number2>number3):
        if(number1>number3):
            print(number2," ",number1, " ",number3)
        else:
            print(number2," ",number3, " ",number1)   
    else:
        print(number3," ",number2, " ",number1)


if True:
    print("Haha done")