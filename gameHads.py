import random

randomInt = random.randint(0,100)

name = input("enter your name: ")
hads = int(input("inter your hads: "))

repetition = 0

while hads != randomInt:
    if hads > randomInt:
        print("-- The input number is larger --")
    else:
        print("-- The input number is smaller --")
    hads = int(input("inter your hads: "))
    repetition += 1

print("wowwwwww", name, "You Won!!!")
print("Your number of repetitions:", repetition)