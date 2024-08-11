n=3
for i in range(1,11):
    print(f"{n}*{i}","=",n*i) #method_1
    print(f"{n}*{i} = {n*i}") #method_2
print("")
i=1
while(i<11):
    print(f"{n}*{i} = {n*i}")
    i+=1

i=1
j=10
while(i<11):
    print(f"{n}*{j} = {n*j}")
    i+=1
    j-=1

for i in range(1,11):
    print(f"{n}*{11-i} = {n*(11-i)}")

