def merge_sorted(collection1, collection2):
    sorted_collection = []
    i, j = 0, 0
    while i < len(collection1) and j < len(collection2):
        if collection1[i] < collection2[j]:
            sorted_collection.append(collection1[i])
            i += 1
        else:
            sorted_collection.append(collection2[j])
            j += 1
        print(sorted_collection)
    while i < len(collection1):
        sorted_collection.append(collection1[i])
        i += 1
    while j < len(collection2):
        sorted_collection.append(collection2[j])
        j += 1
    return sorted_collection


c1 = [2, 4, 6, 8, 10, 11]
c2 = [1, 3, 5, 7, 8, 9]
print(f'Merged list: {merge_sorted(c1, c2)}')

# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8, 8]
# [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
# Merged list: [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11]