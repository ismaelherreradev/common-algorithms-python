def bubble_sort(collection):
    swap_happend = True
    while swap_happend:
        swap_happend = False
        print(str(collection))
        for num in range(len(collection) - 1):
            if collection[num] > collection[num + 1]:
                swap_happend = True
                collection[num], collection[num + 1] = collection[num + 1], collection[num]


c = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

bubble_sort(c)

# [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# [6, 1, 4, 8, 7, 8, 9, 3, 2, 5, 10]
# [1, 4, 6, 7, 8, 8, 3, 2, 5, 9, 10]
# [1, 4, 6, 7, 8, 3, 2, 5, 8, 9, 10]
# [1, 4, 6, 7, 3, 2, 5, 8, 8, 9, 10]
# [1, 4, 6, 3, 2, 5, 7, 8, 8, 9, 10]
# [1, 4, 3, 2, 5, 6, 7, 8, 8, 9, 10]
# [1, 3, 2, 4, 5, 6, 7, 8, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
