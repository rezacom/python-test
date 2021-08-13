
bigAge = 0

ageInput = int(input())

while ageInput != '-1':

    if ageInput == -1:
        break

    if ageInput > bigAge:
        if ageInput >= 10 and ageInput <= 90:
            bigAge = ageInput
    ageInput = (input())

print(bigAge)