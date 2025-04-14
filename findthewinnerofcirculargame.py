n=int(input())
k=int(input())
def helper(n,k):
    if n ==1:
        return 0
    return (helper(n-1,k)+k)%n
ans=helper(n,k)+1
print(ans)  

# Sample Input:
# 5
# 2

# Expected Output:
# 3
