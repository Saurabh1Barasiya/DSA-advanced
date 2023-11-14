def binary_search_algo(arr,target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        # mid = (start + end) // 2
        mid = start + (end - start) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 50
    result = binary_search_algo(arr,x)
    if result != -1:
        print("element present in the array")
    else:
        print("element not present in the array")
