'''x = int(input("Enter num1:"))
y = int(input("Enter num2:"))
z = int(input("Enter num3:"))
s = x+y+z
print(s)
average = s/3
print(float(average))

#complex
ii = int(input("Enter real part"))
jj = int(input("Enter imaginary part"))
complex_num = complex(ii,jj)
print(complex_num)

#string
S = input("Enter string:")
#string slicing:
print(S[0:5])

#list
L = [10,20,30,40,50]
print(L)
Slice = L[0:2]
print(Slice)

#tuple:
T = (1,2,3,4, "python", 23)
print(T)

#dictionary
D = {1:'Rohan', 2:'Mohan', 3:'Sakred'}
for i in D:
    print(i,D[i])


#boolean
T = True
F = False
print(bool(T or F))
print(bool(T and F))

#binary 
print(bin(x))

#Finding discount
purchase = eval(input("Enter purchase amount:"))
if (purchase>=5000):
    purchase -= 500
    print("Final purchase amount:",purchase)
else:
    print("Amount to pay:",purchase)


marks = eval(input("Enter number:"))
if marks>=90:
    print("S grade")
elif marks<=89 and marks<=

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end = "")
    print()
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end = "")
    print()









