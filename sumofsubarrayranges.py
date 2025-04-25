n=int(input())
nums=list(map(int,input().split()))
total=0
for i in range(n):
    maxvalue=float('-inf')
    minvalue=float('inf')
    for j in range(i,n):
        maxvalue=max(maxvalue,nums[j])
        minvalue=min(minvalue,nums[j])
        total+=maxvalue-minvalue 
print(total)          