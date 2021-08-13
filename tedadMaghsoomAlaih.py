
def countMa(num):
    count = 0
    ii = 1

    while ii <= num:
        if num % ii == 0:
            count += 1
        ii += 1

    return count

i = 0
number = 0
counter = 0

while i < 20:
    i += 1
    num = int(input())
    countFunc = countMa(num)
    if counter < countFunc:
        counter = countFunc
        number = num
    elif counter == countFunc:
        if num > number:
            counter = countFunc
            number = num
    
print(number, counter)

