

string = str(input())

string = string.split('+')

newStr = []

for a in string:
    newStr.append(int(a))

for i in range(0, len(newStr)):    
    for j in range(i+1, len(newStr)):    
        if(newStr[i] > newStr[j]):    
            temp = newStr[i];    
            newStr[i] = newStr[j];    
            newStr[j] = temp;    

result=[]

for i in range(len(newStr)
):
    result.append(str(newStr[i]))
    if(i != len(newStr) -1):
        result.append("+")
print(''.join(result))


