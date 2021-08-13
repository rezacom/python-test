
personList = []
ageInput = int(input())

while ageInput != -1:

    if ageInput == -1:
        break

    if ageInput >= 10 and ageInput <= 90:
        personList.append(ageInput)

    ageInput = int(input())

personList.sort()
print(personList[-1], personList[-2])