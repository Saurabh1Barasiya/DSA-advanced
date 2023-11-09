# Apply 1-based indexing.
def first_repeat_element_optimizd(arr):
    i = 0
    n = len(arr)

    # creating a map.
    dict_map = {}
    for i in range(n):
        dict_map[arr[i]] = 0


    for i in range(n):
        dict_map[arr[i]] += 1

    # again iterate for left --> start  of the array .

    for i in range(n):
        if dict_map[arr[i]] > 1:
            element,index = arr[i],i+1
            return [element,index]
            

if __name__ == "__main__":
    arr = [1,5,3,4,3,5,6]
    element,index = first_repeat_element_optimizd(arr)
    print(f"First repeating element {element} and index is {index}")
