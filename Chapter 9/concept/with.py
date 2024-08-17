f=open('D:/vscode/Python__/Chapter 9/concept/test.txt')
print(f.read())
f.close()

# with "with" statement

with open('D:/vscode/Python__/Chapter 9/concept/test.txt') as f:
    print(f.read())
    