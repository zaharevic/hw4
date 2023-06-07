def FillPlenty(plenty, size):
    for i in range(0,size):
        plenty.add(int(input(f"Введите элемент № {i+1}: ")))

a = set()
b = set()
FillPlenty(a, int(input("Введите размер множества № 1: ")))
FillPlenty(b, int(input("Введите размер множества № 2: ")))
temp = a.intersection(b)
print(f"Числа, которые есть в обоих множествах: {temp}")