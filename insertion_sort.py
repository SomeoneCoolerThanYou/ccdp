li=eval(input())
for i in range(len(li)):
     
     temp=li[i]
     j=i-1
     while(li[j]>temp and j>=0):
          li[j+1]=li[j]
          j-=1
     li[j+1]=temp
print(li)
