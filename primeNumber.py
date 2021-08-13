
def countMa(num):
    count = 0
    ii = 1

    while ii <= num:
        if num % ii == 0:
            count += 1
        ii += 1

    return count

count = countMa(int(input()))

if count > 2:
    print("not prime")
else:
    print("prime")