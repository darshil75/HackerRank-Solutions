check = int(input())
for _ in range(check):
    num = int(input())

    p3 = (num - 1) // 3
    p5 = (num - 1) // 5
    p15 = (num - 1) // 15

    sum3 = 3 * p3 * (p3 + 1) // 2
    sum5 = 5 * p5 * (p5 + 1) // 2
    sum15 = 15 * p15 * (p15 + 1) // 2

    total = sum3 + sum5 - sum15
    print(total)