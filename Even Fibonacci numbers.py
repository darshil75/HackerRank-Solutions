check = int(input())
for x in range(0, check):
    num = int(input())

    sum = 0
    a, b = 0, 1
    while a < num:
        if a % 2 == 0:
            sum += a
        a, b = b, a + b
        
    print(sum)