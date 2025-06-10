def prime(val,counter):
    if(counter==val):
        return "It's a prime number"
    if(val%counter==0):
        return "Not a prime number"
    else:
        return prime(val,counter+1)
print("Enter a number: ",end="")
a=int(input())
print(prime(a,2))