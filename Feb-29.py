'''def funcky(a,b):

    print(bin(a))
    print(bin(b))

def b():
    print(bool(x-y))

x = int(input("Enter 1st number:"))
y = int(input("Enter 2nd number:"))

funcky(x,y)
b()


#exponent using recursion
def exp(b,e):
    if e == 0:
        return 1
    elif (e<0):
        return 1/exp(b,-e)
    else:
        return (b*exp(b,e-1))

b = int(input("Enter base:"))
e = int(input("Enter exponent:"))
print(exp(b,e))
#program to soet a list of number in ascending order
'''

s = "I am sorry"
for i in range(1,101):
    print(i,s,end = " ")
    print()