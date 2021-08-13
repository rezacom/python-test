import random

repetition = 0
resultFlag = True

a = 0
b = 99

while resultFlag:

    randomInt = random.randint(a, b)

    yourAnswer = input("Is this answer correct? ")

    if yourAnswer == 'k':
        print("-- The number is smaller --")
        b = randomInt
    elif yourAnswer == 'b':
        print("-- The number is larger --")
        a = randomInt
    elif yourAnswer == 'd':
        print("wowwwwww You Won!!!")
        resultFlag = False

    repetition += 1

print("Your number of repetitions:", repetition)