from random import randint

def YieldRandomize(count, dct):
    for i in range(0, count):
        dct[i] = randint(0, 100)

def CircleCounter(dct, size):
    sum_list = []
    for i in range(0, size):
        if (i == size - 1):
            sum = dct[i] + dct[i - 1] + dct[0]
        elif(i == 0):
            sum = dct[i] + dct[size - 1] + dct[i +1]
        else:
            sum = dct[i] + dct[i - 1] + dct[i + 1]
        sum_list.append(sum)
        sum_list.sort()
    return sum_list[-1]

size, dct = int(input()), {}
YieldRandomize(size, dct)
print(dct)
print(CircleCounter(dct, size))
