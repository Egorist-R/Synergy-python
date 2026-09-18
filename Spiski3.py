weight1 = int(input())
n = int(input())
weights = []
for i in range(n):
    weingt2 = int(input())
    weights.append(weingt2)
weights.sort()
left = 0 
right = n - 1 
boats = 0 
while left <= right:
    if left == right:
        boats = boats + 1
        break
    if weights[left] + weights[right] <= weight1:
        left = left + 1 
        right = right - 1 
    else:
        right = right - 1 
    boats = boats + 1 
print(boats)