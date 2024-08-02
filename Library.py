D = int(input("Enter return date"))
M = int(input("Enter return month"))
Y = int(input("Enter return year:"))

#expected date
AD = 23
AM = 3
EY = 2024

if(EY!=Y):
    print("Fine is 10000")
else:
    if((D <AD) and (M == AM)):
        print("No fine is charged")
    elif((D>AD) and(M==AM)):
        print("fine is charged:",15*(D-AD))
    elif (M>AM):
        print("Fine:",500*(M-AM))

    
    


