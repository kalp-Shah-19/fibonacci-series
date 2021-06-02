def fib(n):
    first=0
    second=1
    if n < 1:
        return -1
    if n==1:
        return first
    if n == 2:
        return second

    count=3
    while count <= n:
        fib_n = first+second
        first = second
        second = first + second
        count = count + 1
    return fib_n
n = input("Enter the term no.:",)
y = int(n)
print(fib(y))

