A, B = map(int, input().split())
numbers = []
for i in range(A, B + 1):
    if i % 2 == 0:
        numbers.append(str(i))
print("".join(numbers))
