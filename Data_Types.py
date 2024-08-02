#integer
x =  int(input("Enter 1st value:"))
y = int(input("Enter 2nd value:"))

print("Sum:",x+y)
print("Product:",x*y)
print("Division:",x/y)

#float
a = float(input("Enter first:"))
b = float(input("Enter second:"))
print("Sum:",a+b)
print("Product:",a*b)
print("Division:",a/b)

#string
s = input("Enter String")
print("String:",s)
print("Sliced:",s[0:4])

#list
L = [10,20,30,40,50]
print("List:",L)
print("Sliced list:",L[0:2])
print("element at a index:",L[2])

#dictionary
D = {1:'Rohan', 2:'Mohan', 3:'Sakred'}
for i in D:
    print(i,D[i])

#boolean
T = True
F = False
print(bool(T or F))
print(bool(T and F))

#Set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("set1 =", set1)
print("set2 =", set2)
print("Union set1 | set2:", set1 | set2)
print("Intersection set1 & set2:", set1 & set2)
print("Difference set1 - set2:", set1 - set2)