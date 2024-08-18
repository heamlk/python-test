for j in range(2,21):
    s=""
    for i in range(1,11):
        s+=f"{j}*{i} = {j*i}\n"
    with open(f"D:/vscode/Python__/Chapter 9/Practise set/tables/{j}.txt","w") as f:
        f.write(s)