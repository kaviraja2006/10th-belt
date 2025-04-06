a=list(map(int,input().split()))
target=int(input())
a.sort()
closest=float('inf')
for i in range(len(a)-2):
    left,right=i+1,len(a)-1
    while left<right:
        total=a[i]+a[left]+a[right]
        if total==target:
            print(total)
            exit()
        if abs(total-target) < abs(closest-target):
            closest=total
        if total<target:
            left+=1
        else:
            right-=1
if closest!= float('inf')  :
    print(closest) 
else:
    print(None)                       
    
# input:    
# -1 2 1 -4
# 1
# output:
# 2    