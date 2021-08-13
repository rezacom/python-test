num = int(input())

num = str(num % 10) + str(num // 10 % 10) + str(num // 10 // 10)

print(int(num) * 2)