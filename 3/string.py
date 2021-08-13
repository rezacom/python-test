
string = input()

stringArr = []

string = string.lower()

string = string.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')

for char in string:
    stringArr.append('.')
    stringArr.append(char)

print(''.join(stringArr))