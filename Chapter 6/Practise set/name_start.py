l=["Helo",'Sachin','Shubham',"shanu",'Lolo']
for i in l:
    if(i[0]=='s' or i[0]=='S'):
        print(f"Good morning {i}")

for i in l:
    if(i.startswith("S") or i.startswith("s")):
        print(f"Good morning {i}")