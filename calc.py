a=input("input: ")
x,y,z=a.split(" ")

if y=="+":
    b=int(x)+int(z)
    print(b)

if y=="-":
    b=int(x)-int(z)
    print(b)

if y=="*":
    b=int(x)*int(z)
    print(b)

if y=="/":
    if z=="0":
        print("you can't divide by 0 you dingleberry")
    else:
        b=int(x)/int(z)
        print(b)