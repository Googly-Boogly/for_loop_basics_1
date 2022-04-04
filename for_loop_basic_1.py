


def num1():
    for i in range(151):
        print(i)


def num2():
    for i in range(5, 1000, 5):
        print(i)

def num3():
    for i in range(100):
        if i % 5 == 0:
            if i % 10 == 0:
                print('Coding Dojo')
            else:
                print('Coding')
        else:
            print(i)


def num4():
    total = 0
    for i in range(500000):
        if i % 2 != 0:
            total = total + i
    print(total)


def num5():
    for i in range(2018, 0, -4):
        print(i)


def num6(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)

num6(2, 9, 3)