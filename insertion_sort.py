
def insertion_sort(collection):
    for insert_index, insert_value in enumerate(collection[1:]):
        print(collection)
        temp_index = insert_index
        while insert_index >= 0 and insert_value < collection[insert_index]:
            collection[insert_index + 1] = collection[insert_index]
            insert_index -= 1
        if insert_index != temp_index:
            collection[insert_index + 1] = insert_value



c = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]


insertion_sort(c)

# [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# [1, 6, 8, 4, 10, 7, 8, 9, 3, 2, 5]
# [1, 4, 6, 8, 10, 7, 8, 9, 3, 2, 5]
# [1, 4, 6, 8, 10, 7, 8, 9, 3, 2, 5]
# [1, 4, 6, 7, 8, 10, 8, 9, 3, 2, 5]
# [1, 4, 6, 7, 8, 8, 10, 9, 3, 2, 5]
# [1, 4, 6, 7, 8, 8, 9, 10, 3, 2, 5]
# [1, 3, 4, 6, 7, 8, 8, 9, 10, 2, 5]
# [1, 2, 3, 4, 6, 7, 8, 8, 9, 10, 5]