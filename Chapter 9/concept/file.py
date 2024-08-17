f=open("D:/vscode/Python__/Chapter 9/concept/test2.py")
data=f.read()
print(data)
f.close()

f=open('D:/vscode/Python__/Chapter 9/concept/test.txt')
data=f.read()
print(data)
f.close()

s="Huraaay"
f=open('D:/vscode/Python__/Chapter 9/concept/test_2.txt',"w")
data=f.write(s)
f.close()

f=open("D:/vscode/Python__/Chapter 9/concept/test2.py")
line=f.readline()
print(line, type(line))

line1=f.readline()
print(line1, type(line1))


f.close()

print("Loop starts here")
#doing this same using while loop
f=open("D:/vscode/Python__/Chapter 9/concept/test2.py")
line=f.readline()
while(line!=""):
    print(line,end="")
    line=f.readline()

f.close()

f=open('D:/vscode/Python__/Chapter 9/concept/test.txt', "a")
data=f.write(s)
f.close()