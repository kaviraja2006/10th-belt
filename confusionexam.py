def confusion(char):
    a=input()
    k=int(input())
    count=0
    maxlength=0
    left=0
    for right in range(len(a)):
        if a[right]!=char:
            count+=1 
        while count>k:
            if a[left]!=char:
                count-=1 
            left+=1 
        maxlength=max(maxlength,right-left+1)  
    return maxlength
ans=max(confusion('T'),confusion('F'))
print(ans)


# Input:
# TTFTFTT
# 1

# Output:
# 5
