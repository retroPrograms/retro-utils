def byteValue(n):
    str = "0b"

    for c in n:
        if c == "g":
            str += "00"
        elif c == "y":
            str += "01"
        elif c == "b":
            str += "10"
        elif c == "r":
            str += "11"
    n = int(str, 2)
    print(n)

    return str

def codeByte(str):
    x=4
    res=[str[y-x:y] for y in range(x, len(str)+x,x)]
    for n in res:
        print(byteValue(n))


print("Enter 16 colour codes, q to stop")
while True:
    print("1234567890123456")
    #line = "yyyyyrrrrbbbbbgg" #input()
    line = input()
    if line == 'q':
        break
    print(line)
    codeByte(line)
    break