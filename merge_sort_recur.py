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



def divide_collection(collection):
    if len(collection) < 2:
        return collection[:]
    else:
        middle = len(collection) // 2
        collection1 = divide_collection(collection[:middle])
        collection2 = divide_collection(collection[middle:])
        return merge_sorted(collection1, collection2)
    

print(divide_collection([3, 7, 2, 4, 6, 7]))

# [2]
# [2]
# [2, 3]
# [6]
# [4]
# [2]
# [2, 3]
# [2, 3, 4]
# [2, 3, 4, 6]
# [2, 3, 4, 6, 7]
# [2, 3, 4, 6, 7, 7]