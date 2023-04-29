def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n - 1)


z = 0
print(f"{z}! is {factorial_recur(z)}")

z = 1
print(f"{z}! is {factorial_recur(z)}")

z = 5
print(f"{z}! is {factorial_recur(z)}")

# 0! is 1
# 1! is 1
# 5! is 120