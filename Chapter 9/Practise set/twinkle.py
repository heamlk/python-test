with open("D:/vscode/Python__/Chapter 9/Practise set/1st.txt") as f:
    data=f.read()
    if(data.find("twinkle")>=0 or data.find("Twinkle")>=0):
        print("Yes it has the word")
    else:
        print("No no sorry")

with open("D:/vscode/Python__/Chapter 9/Practise set/2nd.txt") as f:
    data=f.read()
    if(data.find("twinkle")>=0 or data.find("Twinkle")>=0):
        print("Yes it has the word")
    else:
        print("No no sorry")
    
# Another way

with open("D:/vscode/Python__/Chapter 9/Practise set/1st.txt") as f:
    data=f.read()
    if("twinkle" in data or "Twinkle" in data):
        print("Yes it has the word")
    else:
        print("No no sorry")