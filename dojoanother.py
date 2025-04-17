# You are given a string representing a non-negative
# integer and an integer
# Your task is to return the smallest possible integer after removing
# Input Format
# 1 . A string representing the non-negative integer.
# 2. An integer k the number of digits to remove.
# Output Format
# • A string representing the smallest possible integer after
# removing digits, with no leading zeroes.
# • If the resulting integer is empty, output

# Example 1
# Input:
# "1432219"
# 3
# Output:
# "1219"

num=input()
k=int(input())
stack=[]
for i in num:
    while k>0 and stack and stack[-1]>i:
        stack.pop()
        k-=1
    stack.append(i)
if k:
    stack=stack[:-k]  
result=''.join(stack).lstrip('0')    
if result:
    print(result)
else:
    print("0")          
    