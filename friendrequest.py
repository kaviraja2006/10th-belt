# n = int(input())
# ages = list(map(int, input().split()))
# count = 0

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         if ages[j] <= 0.5 * ages[i] + 7:
#             continue
#         if ages[j] > ages[i]:
#             continue
#         if ages[j] > 100 and ages[i] < 100:
#             continue
#         count += 1

# print(count)


n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(n):
    for j in range(n):
        if i==j:
            continue 
        if a[j]<=0.5*a[i]+7:
            continue
        if a[j]>a[i]:
            continue 
        if a[j]>100 and a[i]<100:
            continue
        count+=1   
print(count)                    