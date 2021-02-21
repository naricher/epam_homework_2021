def print_spiral(size):
    count = 1
    i=0
    j=-1
    max_j=size - 1
    max_i=size - 1
    min_j=0
    min_i=1
    spiral= [[0 for j in range(size)] for i in range(size)]
    while True:
        #==>
        while j < max_j:
            j += 1
            spiral[i][j] = count
            count += 1
        max_j -= 1
        #Down
        while i < max_i:
            i += 1
            spiral[i][j] = count
            count += 1
        max_i -= 1
        #<==
        while j > min_j:
            j -= 1
            spiral[i][j] = count
            count += 1
        min_j += 1
        #Up
        while i > min_i:
            i -= 1
            spiral[i][j] = count
            count += 1
        min_i += 1
        if j == (size - 1) // 2 and i == size // 2:
            break
        
    n = range(len(spiral))
    for i in n:
        for j in n:
            print (spiral[i][j],end=' ')
        print()

n = int(input("Enter number:"))
print_spiral(n)

