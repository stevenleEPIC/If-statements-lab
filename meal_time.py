def main():
    t = input("what time is it?: ")
    t=convert(t)
    print(t)

def convert(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    t = h + m / 60
    return t

if __name__ == "__main__":
    main()
    if time>= 7.0 and t<= 8.0:
        print("breakfast time")
    elif time>= 12.0 and t<= 13.0:
        print("dinner time")
