x=int(input("what's the high temp? (F): "))
if x < 60:
    print("you need to bring a sweater")
elif x >= 60 and x < 140:
    print("you don't need to bring a sweater")
elif x >= 140:
    print("invalid input, how can u survive that son ToT")