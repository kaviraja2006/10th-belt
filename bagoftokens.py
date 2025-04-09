a=list(map(int,input().split()))
power=int(input())
left=0
right=len(a)-1
maxscore=0
score=0
while left<=right:
    if power>=a[left]:
        power-=a[left]
        left+=1
        score+=1
        maxscore=max(maxscore,score)
    elif score>0:
        power+=a[right]
        right-=1
        score-=1
        maxscore=max(maxscore,score)
    else:
        break
print(maxscore)                

# Input:
# 100 200 300 400
# 200

# Output:
# 2
