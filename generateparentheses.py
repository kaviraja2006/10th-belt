def generateparenthesis(n,open,close,s,res):
    if open==n and close ==n:
        res.append(s)
        return 
    if open<n:
        generateparenthesis(n,open+1,close,s+"(",res) 
    if close<open:
        generateparenthesis(n,open,close+1,s+")",res)    
    return res
    
n=int(input())
print(generateparenthesis(n,0,0,"",[]) )   

# Input:
# Enter number of pairs: 3

# Output:
# ['((()))', '(()())', '(())()', '()(())', '()()()']
