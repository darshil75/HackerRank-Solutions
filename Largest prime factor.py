check = int(input())
for _ in range(check):
    n = int(input())

    i = 2
    while i * i <= n:
        if n % i == 0:
            n = n // i
        else:
            i += 1

    print(n)