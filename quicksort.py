def quicksort(colletion):
    if len(colletion) < 2:
        return colletion
    else:
        pivot = colletion[-1]
        smaller, equal, larger = [], [], []
        for num in colletion:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)


c = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
print(quicksort(c))
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]