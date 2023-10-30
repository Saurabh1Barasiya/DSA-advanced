# get union without duplicates.

def get_union(arr1,arr2):
    new_arr = []

    m = len(arr1)

    n = len(arr2)

    i = j = 0

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            new_arr.append(arr2[j])
            j += 1
        else:
            new_arr.append(arr1[i])
            i += 1
            j += 1
        

    while i < m:
        new_arr.append(arr1[i])
        i += 1
        
    while j < n:
        new_arr.append(arr2[j])
        j += 1


    return new_arr



if __name__ == "__main__":
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]


    final_array = get_union(arr1,arr2)
    print(final_array)