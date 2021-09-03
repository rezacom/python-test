
string = str(input())

reverseString = string[::-1]

if(string.lower() == reverseString.lower()):
    print("palindrome")

else:
    print("not palindrome")

