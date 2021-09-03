
typeStr = str(input())

# print(typeStr.find("hello"))

helloWord = ""

# for i in typeStr:

find_h = typeStr.find("h")
find_e = typeStr.find("e")
find_l = typeStr.find("l")
find_l2 = typeStr.find("l", find_l)
find_o = typeStr.find("o")


if typeStr.find("h") != -1:
    helloWord += "h"

if typeStr.find("e", find_h) != -1: 
    if typeStr.find("h") < typeStr.find("e", find_h):
        # print("e", typeStr.find("e"))
        helloWord += "e"

if typeStr.find("l", typeStr.find("e", find_h)) != -1: 
    if typeStr.find("e", find_h) < typeStr.find("l", typeStr.find("e", find_h)):
        # print("l", typeStr.find("l"))
        helloWord += "l"

if typeStr.find("l", typeStr.find("l", typeStr.find("e", find_h))) != -1: 
    # print("l", typeStr.find("l", typeStr.find("l", typeStr.find("e", find_h))))
    helloWord += "l"

if typeStr.find("o") != -1: 
    if typeStr.find("l", typeStr.find("l", typeStr.find("e", find_h))) < typeStr.find("o", typeStr.find("l", typeStr.find("e", find_h))):
        # print("o", typeStr.find("o"))
        helloWord += "o"

if helloWord == "hello":
    print("YES")
else:
    print("NO")
