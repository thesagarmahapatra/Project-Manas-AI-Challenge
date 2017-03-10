#Automate the Boring Task
#Shape Detection
flag = 0
n = 180
a = []
b = []
c = []
m = n + 2
S = 0
I = 0
J = 0
z = 0
p = 0


def main():
    global flag
    for i in xrange(n):
        a.append([])
        for j in xrange(n):
            input = int(raw_input())
            # input = 0
            a[i].append(input)

    b = [[0 for i in xrange(m)] for j in xrange(m)]

    for i in xrange(n):
        for j in xrange(n):
            b[i + 1][j + 1] = a[i][j]

    while S == 0:
        scan()
        if flag == 1:
            z = 10
            scan()
        elif flag == 3:
            z = 2
            scan()
        elif flag == 4:
            flag = 0
            p = 1
            scan()
            p = 0
            if c[0] == c[1]:
                z = 3
                scan()
            else:
                z = 4
                scan()
        elif flag == 5:
            z = 5
            scan()
        elif flag == 6:
            z = 6
            scan()
        elif flag == 8:
            z = 8
            scan()
            p = 0
            z = 0
            flag = 0
            I = 0
            J = 0

    for i in xrange(m):
        for j in xrange(m):
            if b[i][j] == 10:
                b[i][j] = 1
        for i in xrange(n):
            for j in xrange(n):
                print str(b[i + 1][j + 1]) + " "
            print "\r\n"


def scan():
    for i in xrange(m):
        for j in xrange(m):
            if b[i][j] == 1:
                I = i
                J = j
                break

            if I != 0:
                break

        if I != 0 or J != 0:
            analyze(I, J)

        else:
            S = 1


def analyze(x, y):
    if b[x][y + 1] == 1:
        right(x, y)

    elif b[x + 1][y + 1] == 1:
        bottomright(x, y)

    elif b[x + 1][y] == 1:
        bottom(x, y)

    elif b[x + 1][y - 1] == 1:
        bottomleft(x, y)


def upperleft(x, y):
    global flag
    while b[x - 1][y - 1] != 0:
        if z != 0:
            if z == 10:
                if b[x][y] == 1:
                    b[x][y] = z
            elif z > b[x][y]:
                b[x][y] = z
        if p == 1:
            c[flag] += 1
        x -= 1
        y -= 1

    if z != 0:
        b[x][y] = z

    flag += 1

    if (x == I and y == J):
        pass
    elif b[x - 1][y] == 1:
        upper(x, y)
    elif b[x - 1][y + 1] == 1:
        upperright(x, y)
    elif b[x][y + 1] == 1:
        right(x, y)
    elif b[x + 1][y] == 1:
        bottom(x, y)
    elif b[x + 1][y - 1] == 1:
        bottomleft(x, y)
    elif b[x][y - 1] == 1:
        left(x, y)
    elif x != I and y != J and flag > 1:
        flag = 1


def upper(x, y):
    global flag
    while b[x - 1][y] != 0:
        if z != 0:
            if z == 10:
                if b[x][y] == 1:
                    b[x][y] = z
            elif z > b[x][y]:
                b[x][y] = z
        if p == 1:
            c[flag] += 1
        x -= 1

    if z != 0:
        b[x][y] = z

    flag += 1

    if x == I and y == J:
        pass
    elif b[x - 1][y - 1] == 1:
        upperleft(x, y)
    elif b[x - 1][y + 1] == 1:
        upperright(x, y)
    elif b[x][y + 1] == 1:
        right(x, y)
    elif b[x + 1][y + 1] == 1:
        bottomright(x, y)
    elif b[x + 1][y - 1] == 1:
        bottomleft(x, y)
    elif b[x][y - 1] == 1:
        left(x, y)
    elif x != I and y != J and flag > 1:
        flag = 1


def upperright(x, y):
    global flag
    while b[x - 1][y + 1] != 0:
        if z != 0:
            if z == 10:
                if b[x][y] == 1:
                    b[x][y] = z
            elif z > b[x][y]:
                b[x][y] = z
        if p == 1:
            c[flag] += 1
        x -= 1
        y += 1
    if z != 0:
        b[x][y] = z
    flag += 1

    if x == I and y == J:
        pass
    elif b[x - 1][y - 1] == 1:
        upperleft(x, y)
    elif b[x - 1][y] == 1:
        upper(x, y)
    elif b[x][y + 1] == 1:
        right(x, y)
    elif b[x + 1][y + 1] == 1:
        bottomright(x, y)
    elif b[x + 1][y] == 1:
        bottom(x, y)
    elif b[x][y - 1] == 1:
        left(x, y)
    elif x != I and y != J and flag > 1:
        flag = 1


def right(x, y):
    global flag
    while b[x][y + 1] != 0:
        if z != 0:
            if z == 10:
                if b[x][y] == 1:
                    b[x][y] = z
            elif z > b[x][y]:
                b[x][y] = z
        if p == 1:
            c[flag] += 1
        y += 1
    if z != 0:
        b[x][y] = z
    flag += 1
    if x == I and y == J:
        pass
    elif b[x - 1][y - 1] == 1:
        upperleft(x, y)
    elif b[x - 1][y] == 1:
        upper(x, y)
    elif b[x - 1][y + 1] == 1:
        upperright(x, y)
    elif b[x + 1][y + 1] == 1:
        bottomright(x, y)
    elif b[x + 1][y] == 1:
        bottom(x, y)
    elif b[x + 1][y - 1] == 1:
        bottomleft(x, y)
    elif x != I and y != J and flag > 1:
        flag = 1


def bottomright(x, y):
    global flag
    while b[x + 1][y + 1] != 0:
        if z != 0:
            if z == 10:
                if b[x][y] == 1:
                    b[x][y] = z
            elif z > b[x][y]:
                b[x][y] = z
        if p == 1:
            c[flag] += 1
        x += 1
        y += 1

    if z != 0:
        b[x][y] = z

    flag += 1

    if x == I and y == J:
        pass
    elif b[x - 1][y] == 1:
        upper(x, y)
    elif b[x - 1][y + 1] == 1:
        upperright(x, y)
    elif b[x][y + 1] == 1:
        right(x, y)
    elif b[x + 1][y] == 1:
        bottom(x, y)
    elif b[x + 1][y - 1] == 1:
        bottomleft(x, y)
    elif b[x][y - 1] == 1:
        left(x, y)
    elif x != I and y != J and flag > 1:
        flag = 1


def bottom(x, y):
    global flag
    while b[x + 1][y] != 0:
        if z != 0:
            if z == 10:
                if b[x][y] == 1:
                    b[x][y] = z
            elif z > b[x][y]:
                b[x][y] = z
        if p == 1:
            c[flag] += 1
        x += 1
    if z != 0:
        b[x][y] = z
    flag += 1
    if x == I and y == J:
        pass
    elif b[x][y - 1] == 1:
        left(x, y)
    elif b[x - 1][y - 1] == 1:
        upperleft(x, y)
    elif b[x - 1][y + 1] == 1:
        upperright(x, y)
    elif b[x][y + 1] == 1:
        right(x, y)
    elif b[x + 1][y + 1] == 1:
        bottomright(x, y)
    elif b[x + 1][y - 1] == 1:
        bottomleft(x, y)
    elif x != I and y != J and flag > 1:
        flag = 1


def bottomleft(x, y):
    global flag
    while b[x + 1][y - 1] != 0:
        if z != 0:
            if z == 10:
                if b[x][y] == 1:
                    b[x][y] = z
            elif z > b[x][y]:
                b[x][y] = z
        if p == 1:
            c[flag] += 1
        x += 1
        y += 1
    if z != 0:
        b[x][y] = z
    flag += 1
    if x == I and y == J:
        pass
    elif b[x - 1][y - 1] == 1:
        upperleft(x, y)
    elif b[x - 1][y] == 1:
        upper(x, y)
    elif b[x][y + 1] == 1:
        right(x, y)
    elif b[x + 1][y + 1] == 1:
        bottomright(x, y)
    elif b[x + 1][y] == 1:
        bottom(x, y)
    elif b[x][y - 1] == 1:
        left(x, y)
    elif x != I and y != J and flag > 1:
        flag = 1


def left(x, y):
    global flag
    while b[x][y - 1] != 0:
        if z != 0:
            if z == 10:
                if b[x][y] == 1:
                    b[x][y] = z
            elif z > b[x][y]:
                b[x][y] = z
        if p == 1:
            c[flag] += 1
        y -= 1
    if z != 0:
        b[x][y] = z
    flag += 1

    if x == I and y == J:
        pass
    elif b[x - 1][y - 1] == 1:
        upperleft(x, y)
    elif b[x - 1][y] == 1:
        upper(x, y)
    elif b[x - 1][y + 1] == 1:
        upperright(x, y)
    elif b[x + 1][y + 1] == 1:
        bottomright(x, y)
    elif b[x + 1][y] == 1:
        bottom(x, y)
    elif b[x + 1][y - 1] == 1:
        bottomleft(x, y)
    elif x != I and y != J and flag > 1:
        flag = 1


if __name__ == "__main__":
    main()
