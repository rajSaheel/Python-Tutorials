#This is a global variable as it is not assigned inside a function
var =10
print(1,var)

def output():
    #Here var is a local variable as it is assigned inside a function
    var=20
    print(2,var)
    var=30
    print(3,var)

output()
output()
output()
output()

print(4,var)


"""
1 10
2 20
3 30
4 10

"""