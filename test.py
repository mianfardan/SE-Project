import time
temp = input("Enter a name here ")
result = ""
for i in range(0,len(temp)):
    hold = ord(temp[0:1])
    hold += 1590
    temp = temp[1:len(temp)]
    result += chr(hold)

print(result)

for i in range(0,len(result)):
    hold = ord(result[0:1])
    hold -= 1590
    result = result[1:len(result)]
    temp += chr(hold)

print(temp)

