
def uloha_1(n):
    for i in range(n):
        print("#" * n)


def uloha_2(n):
    for i in range(n):
        if i == 0 or i == (n - 1):
            print("#" * n)
        else:
            print("#", " " * (n - 2), "#", sep="")


def uloha_3(n):
    for i in range(n):
        print("#" * (i + 1))


def uloha_4(n):
    num = 1
    for i in range(n):
        x = i + 1
        print(" " * (n - x), "#" * num, sep="")
        num = num + 2


def uloha_5(n):
    space_before = 0
    space_between = n - 2
    m = n//2
    for i in range(m):
        if space_between >= 1:
            print(" " * space_before, "#", " " * space_between, "#", sep="")
            space_before = space_before + 1
            space_between = space_between - 2

        elif space_between < 1:
            print(" " * space_before, "#", " " * space_between, "#", sep="")
            space_before = space_before - 1
            space_between = space_between + 2

    if (n % 2) == 1:
        print(" " * (n//2), "#", sep="")
        for i in range(m):
            space_before = space_before - 1
            space_between = space_between + 2
            print(" " * space_before, "#", " " * space_between, "#", sep="")

    else:
        print(" " * (space_before + 1), "#", " " * (space_between - 2), "#", sep="")
        for i in range(m - 1):
            print(" " * space_before, "#", " " * space_between, "#", sep="")
            space_before = space_before - 1
            space_between = space_between + 2


def uloha_6(n):
    num = 1
    space_before = ""
    for i in range(n):
        space_before = i + 1
        print(" " * (n - space_before), "#" * num, sep="")
        num = num + 2
    num = num - 2
    space_before = space_before - 1
    for i in range(n):
        num = num - 2
        print(" " * (n - space_before), "#" * num, sep="")
        space_before = space_before - 1


def uloha_7(r):
    diameter = r * 2
    radius = diameter / 2 - .5
    r = (radius + .25) ** 2 + 1
    for i in range(diameter):
        line = ''
        y = (i - radius) ** 2
        for j in range(diameter):
            x = (j - radius) ** 2
            if x + y <= r:
                line = line + '#'
            else:
                line = line + '*'
        print(line)


def uloha_8(n):
    for i in range(n):
        if (i % 2) == 0:
            start = "#"
        else:
            start = "*"

        current = start
        line = ""
        for j in range(n):
            line = line + current
            if current == "#":
                current = "*"
            elif current == "*":
                current = "#"
        print(line)


def uloha_9(n, m):
    start = "#"
    for i in range(n):
        current = start
        left = m
        line = ""
        for j in range(n):
            if left != 0:
                line = line + current
                left = left - 1
            else:
                if current == "#":
                    current = "*"
                    line = line + current
                elif current == "*":
                    current = "#"
                    line = line + current
                left = m - 1
        print(line)
        if start == "#":
            start = "*"
        elif start == "*":
            start = "#"


uloha_7(20)
