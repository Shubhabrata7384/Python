#wap to check if a message is spam or not
p1="subcribe now"
p2="like and share"
p3="comment below"
p4="thank you for watching"

message =input("Enter your message: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("spam message")
else:

    print("not a spam message")