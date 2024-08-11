i=1
while(i<100): #1st loop
    print(i)
    i+=1
for i in range(1,100): #2nd loop
    print(i)
l=[2,3,4,5,"Hello"]
print("New loop")
i=1
while(i<len(l)): #3rd loop
    print(l[i])
    i+=1
for i in l:
    print(i)
d={0:"Helo",1:"Bye"}
for i in d:
    print(i)
else:
    print("done")
