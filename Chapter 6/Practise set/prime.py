n=int(input())
e=int((n/2)+1)
for i in range(2,e):
    if(n%i==0):
        print("Not a prime")
        break
else:
    print("Number is prime")
