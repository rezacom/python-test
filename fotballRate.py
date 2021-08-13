
win = 0
rates = 0

for i in range(1, 31):
    rate = int(input())
    if rate == 3:
        win += 1
    rates += rate

print(rates, win)