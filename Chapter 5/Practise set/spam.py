comment=input()


#method_1
if(comment.lower().find("buy now")>=0 or comment.lower().find("subscribe")>=0):
    print("It's a spam")
else:
    print("Yoo its good")


#method_2
p1="buy now"
p2="subscribe"
if((p1 in comment.lower()) or (p2 in comment.lower())):
    print("SPAM")
else:
    print("Yooo again safe huh")