import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
userseperators="._"
mbile="9"
usrnme=upper+userseperators
length=12
username="".join(random.sample(usrnme,length))
print(username)
email=lower+numbers
length=8
mail="".join(random.sample(email,length))
print(mail+"@gmail.com")
mobile=mbile+numbers
length=9
nam="ph"
mobno="".join(random.sample(mobile,length))
print("9"+mobno)
pswd=lower+numbers
length=10
pad="".join(random.sample(pswd,length))
print(nam+"********")
question=input("crack password?[y/n] ")
if question=="y":
    import sys
    import time
    print("(passwords will be invisible during search)")
    for i in range(10):
        print("Searching..." + "." * i)
        sys.stdout.write("\033[F") # Cursor up one line
        time.sleep(1)
    print("password found")
    print(nam+pad)
elif question=="n":
    print("OK")
else:
    print("[n] is default")

