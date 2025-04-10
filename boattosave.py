a=list(map(int,input().split()))
limit=int(input())
boat=0
a.sort()
left=0
right=len(a)-1
while left<=right:
    if a[left]+a[right]<=limit:
        left+=1
    right-=1
    boat+=1
print(boat)  

# Input:
# 1 2 2 3
# 3

# Output:
# 3
      