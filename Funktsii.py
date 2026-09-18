def find_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
num = int(input("Введите число: "))
start_number = find_factorial(num)
factorials_list = []
for i in range(start_number, 0, -1):
    fact = find_factorial(i)
    factorials_list.append(fact)
print(factorials_list)