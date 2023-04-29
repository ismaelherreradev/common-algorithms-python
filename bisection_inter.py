def bisection_inter(n, collection):
    start = 0
    stop = len(collection) - 1
    while start <= stop:
        mid = (start + stop)//2
        if n == collection[mid]:
            return f"{n} found at index: {mid}"
        elif n > collection[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    return f"{n} not found in list"


c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_to_search = 1


print(bisection_inter(num_to_search, c))
