def max_of_3(val1, val2, val3):
    if((val1>val2)&(val1>val3)):
        return val1
    elif((val2>val3)&(val2>val1)):
        return val2
    else:
        return val3

print("Enter 3 numbers: ")
a=int(input())
b=int(input())
c=int(input())
print("Maximum number is:",max_of_3(a,b,c))

