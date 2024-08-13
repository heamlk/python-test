def remove(s,l):
    c=0
    for i in l:
        if(s==i):
            c+=1
            l.remove(s)
    if(c==0):
        print("Not in the list")
    return l


l=["Whyyy","Olyyy","Hell","Hello","llo"]
print(l)
print(remove(input(),l))