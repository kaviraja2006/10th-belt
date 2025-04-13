height=list(map(int,input().split()))
left,right=0,len(height)-1
maxi=0
while left<right:
    width=right-left
    area=width*min(height[left],height[right])
    maxi=max(maxi,area)
    if height[left]<height[right]:
        left+=1
    else:
        right-=1
print(maxi)

# Sample Input:
# 1 8 6 2 5 4 8 3 7

# Expected Output:
# 49
