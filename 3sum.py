a=list(map(int,input().split()))
a.sort()
result=[]
for i in range(len(a)-2):
    if i>0 and a[i]==a[i-1]: #edge case which helps to make the loop 
        continue             #without going out of the bound
    left,right=i+1,len(a)-1
    while left<right:
            total=a[i]+a[left]+a[right]
            if total==0:
                result.append([a[i],a[left],a[right]])
                while left<right and a[left]==a[left+1]:
                    left+=1
                while left<right and a[right]==a[right-1]:
                    right-=1
                left+=1
                right-=1
            elif total<0:
                left+=1
            else:
                right-=1
print(result)                
                       
                
                    