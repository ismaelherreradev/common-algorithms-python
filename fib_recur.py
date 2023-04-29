def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n - 1) + fib_recur(n - 2)
    

print(f'serie: {fib_recur(10)}')