'''salary = int(input("Enter basic salary:"))
h = int(input("Enter hours of working:"))
paytype = input("Enter minutes or hours:")
#x = input("Enter hourly or weekly:5")
r = int(input("rate:"))
pay = 0
if(paytype== "hours"):
    if h>40:
        pay = r*(40+1.5)*(h-40)
    else:
        pay = r*h
    print(pay)
else:
    print("Pay:", pay)


x = input("Enter string:")
rev = x[::-1]
if x == rev:
    print("Palindrome")
else:
    print("not palindrome")
'''

#fibonacci sequence
x = eval(input("Enter range:"))
a = 0
b = 1

print(a)
print(b)
for i in range(0,x):
    
    c = a+b
    print(c)
    a,b = b,a+b
    

