count = 0
total = 0

number = int(input("enter a number: "))
while number != -1:
    if number:
        count += 1
        total += number
        number = int(input("enter a number: "))
print(total * count)
