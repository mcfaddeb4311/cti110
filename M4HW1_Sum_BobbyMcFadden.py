# Sum of Postive Numbers with Loop. 
# 6-23-2017
# CTI-110 M4HW1 - Sum of Numbers
# Bobby McFadden

num=int(input("Enter number"))
sum=0
while(num!=0):
    remainder=num%10
    sum=sum+remainder
    num=num//10

print("sum of number is : ",sum)


