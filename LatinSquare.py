def randomizeArray(arr):
    import random
    randomized = arr[:]
    random.shuffle(randomized)
    return randomized

def latinSquare(num_squared):
    square = []
    for i in range(num_squared):
        new_row = []
        for j in range(num_squared):
            new_row.append((i + j) % num_squared + 1)
        print(new_row)
        square.append(new_row)
    square = randomizeArray(square)
    return square


print(latinSquare(5))