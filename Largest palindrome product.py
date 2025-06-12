t = int(input())

for _ in range(t):
    n = int(input())
    max_palindrome = 0

    for i in range(999, 99, -1):
        if i * 999 < max_palindrome:
            break  # No need to check smaller i

        for j in range(i, 99, -1):
            product = i * j

            if product < max_palindrome:
                break  # No better palindrome will be found in this loop

            if product < n:
                s = str(product)
                if s == s[::-1]:
                    max_palindrome = product

    print(max_palindrome)
