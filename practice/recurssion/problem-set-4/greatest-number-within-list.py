def find_gretest_number(a, n):
    if n==1:
        return a[0]
    else:
        x = find_gretest_number(a, n-1)

    if x > a[n-1]:
        return x
    else:
        return a[n-1]


a = [12, 10, 30, 50, 100]
greatest_number = find_gretest_number(a, 5)

print(greatest_number)