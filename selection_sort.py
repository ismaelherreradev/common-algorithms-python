def selection_sort(collection):
    marker = 0
    while marker < len(collection):
        for num in range(marker, len(collection)):
            if (collection[num] < collection[marker]):
                collection[marker], collection[num] = collection[num], collection[marker]
        marker += 1
        print(collection)


c = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

selection_sort(c)

# [1, 8, 6, 4, 10, 7, 8, 9, 3, 2, 5]
# [1, 2, 8, 6, 10, 7, 8, 9, 4, 3, 5]
# [1, 2, 3, 8, 10, 7, 8, 9, 6, 4, 5]
# [1, 2, 3, 4, 10, 8, 8, 9, 7, 6, 5]
# [1, 2, 3, 4, 5, 10, 8, 9, 8, 7, 6]
# [1, 2, 3, 4, 5, 6, 10, 9, 8, 8, 7]
# [1, 2, 3, 4, 5, 6, 7, 10, 9, 8, 8]
# [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 8]
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
