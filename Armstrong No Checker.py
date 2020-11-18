t=(int(input("Enter The number:")))
TempNo=t
sum=0
while TempNo>0:
    remainder=TempNo%10
    cube=remainder**3
    TempNo=TempNo//10
    sum=sum+cube
if t==sum:
    print("It is a Armstrong Number")
else:
    print("It is not a Armstrong Number")
    
