def get_last_occrence(arr,target):
    start = 0 
    end = len(arr) - 1
    ans = -1

    while start <= end:
        mid = start + (end - start) // 2

        if target == arr[mid]:
            ans = mid
            # go to right.
            start = mid + 1
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1

    return ans

if __name__ == "__main__":
    arr = [1,3,3,4,4,4,4,4,6,7,7,7,7,7,9]
    key = 7
    res = get_last_occrence(arr,key)
    if res != -1:
        print(f"last index found at index {res}")
    else:
        print(f"{key} is not found")


