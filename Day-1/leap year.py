#to check whether given year is leap year or not
y=int(input("enter the year:"))
if y%4==0 and y%100!=0:
    print("leap year")
else:
    print("not a leap year")
