num=int(input(""))  
tmp=num
sum=0
while(num>0):
    digit=num%10  
    sum+=digit**3 
    num//=10 
if tmp == sum:
    print("yes")
else:
    print("no")
