def maximum_fruits(fruits):
    basket = {}
    left = 0
    max_len = 0
    for right in range(len(fruits)):
        basket[fruits[right]] = basket.get(fruits[right], 0) + 1
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

fruits = list(map(int, input().split()))
print(maximum_fruits(fruits))


# Sample Input 1:
# 1 2 1 2 3
# Output:
# 4

# Sample Input 2:
# 0 1 2 2
# Output:
# 3

# Sample Input 3:
# 1 2 3 2 2
# Output:
# 4

# Sample Input 4:
# 1 1 1 1
# Output:
# 4