# get union without duplicates.

def get_union(arr1,arr2):
    new_arr = []

    for e1 in arr1:
        new_arr.append(e1)

    for e2 in arr2:
        if e2 not in new_arr:
            new_arr.append(e2)
    
    return new_arr



if __name__ == "__main__":
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]


    final_array = get_union(arr1,arr2)
    print(final_array)