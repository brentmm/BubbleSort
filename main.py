from random import randint

#generates list if 10 random numbers
def test():
    a = []
    for i in range(0, 10):
        a.append(randint(0, 10))
    return a

#sorts list of random numbers
def bubbleSort(c):
    n = len(c)
    loop = True
    while loop == True:
        inOrder = True
        for i in range(0, n):
            if i + 1 < n:
                if c[i + 1] < c[i]: #compares values
                    c[i + 1], c[i] = c[i], c[i + 1] #swaps numbers
                    inOrder = False
                print(c)
                print()
        if inOrder == True:
            loop = False

    return c

b = test()

print("Original: " + str(b))
print()
print("Sorted: " + str(bubbleSort(b)))
