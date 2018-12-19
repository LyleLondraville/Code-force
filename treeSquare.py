x1 = 3
y1 = 3

x2 = 10
y2 = 10

if (x1 == x2) and (y1 == y2):
    print (-1)
else :
    if x1 == x2:
        dif = y2 - y1
        x1 += dif
        x2 += dif
        print ('{} {} {} {}'.format(x1, y1, x2, y2))
    elif y1 == y2:
        dif = x2 - x1
        y1 += dif
        y2 += dif
        print('{} {} {} {}'.format(x1, y1, x2, y2))
    elif abs(x1 - x2) == abs(y1 - y2):
        dif = x2 - x1
        y1 += dif
        y2 -= dif
        print('{} {} {} {}'.format(x1, y1, x2, y2))
    else :
        print (-1)

