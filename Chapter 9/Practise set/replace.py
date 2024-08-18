with open("Chapter 9/Practise set/2nd.txt") as f:
    old=f.read()

old=old.replace("donkey","######").replace("Donkey","######")

with open("Chapter 9/Practise set/2nd.txt","w") as f:
    f.write(old)