def fib(n):
    a = 0
    b = 1
    
    print(a)
    print(b)
    while (n>0):
        c = a+b
        a,b = b,c
    
        n -= 1
        
x = int(input())
L = []
for i in range(x+1):
    a = int(input())
    print(L[a])



