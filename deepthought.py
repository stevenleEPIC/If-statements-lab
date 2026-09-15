x=input("what is the answer to life, the universe, and everything? ")

if str(x) == "42":
    print("yes")
elif str(x).lower() == "fourty-two":
    print("yes")
else: 
    print("no")