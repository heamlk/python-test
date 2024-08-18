n=int(input("Enter new score: "))

with open("Chapter 9/Practise set/3rd.txt",) as f:
    data=f.read()

if(data==""):
    data=0
if(n>int(data)):   
    with open("Chapter 9/Practise set/3rd.txt","w") as f:
        f.write(str(n))
        print(f"Your new score is {n} and previous was {data}")
else:
    print(f"You previous score is greater than new one that is previous is {data} and new is {n}")