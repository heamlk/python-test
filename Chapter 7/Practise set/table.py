def table(n,c=1):
    if(c==11):
        return
    print(f"{n}*{c} = {n*c}")
    c+=1
    table(n,c)

table(int(input()))