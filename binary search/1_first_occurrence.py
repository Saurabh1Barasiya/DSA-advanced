def get_first_occrence(arr,target):
    start = 0 
    end = len(arr) - 1 
    ans = -1

    while start <= end:
        mid = start + (end - start) // 2
        if target == arr[mid]:
            # store the answer.
            ans = mid
            # go to left.
            end = mid - 1
        elif target > arr[mid]:
            # go to right.
            start = mid + 1
        elif target < arr[mid]:
            # go to left.
            end = mid - 1
    return ans


if __name__ == "__main__":
    arr = [1,3,3,4,4,4,4,4,6,7,9]
    key = 4
    res = get_first_occrence(arr,key)
    if res != -1:
        print(f"First index found at index {res}")
    else:
        print(f"{key} is not found")