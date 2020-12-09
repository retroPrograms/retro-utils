def byteValue(n):
    i = 0
    cols = {'g':0, 'y':1, 'b':2, 'r':3}
    vals = [128,64,32,16,8,4,2,1]
    index = 0
    for c in n:
        if index == 0:
            i += 64
        print(c)

    return i

def codeByte(str):
    x=4
    res=[str[y-x:y] for y in range(x, len(str)+x,x)]
    for n in res:
        print(byteValue(n))


print("Enter 16 colour codes, q to stop")
while True:
    print("1234567890123456")
    line = input()
    if line == 'q':
        break
    print(line)
    codeByte(line)
