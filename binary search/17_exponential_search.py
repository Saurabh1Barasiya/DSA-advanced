def exponential_search(arr, target,n):
    # find the sub array where elelemt (target) is present.
    # apply binary_searh on the subarray.

    if arr[0] == target:
        return 0
    
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2
    
    # loop break hua to  start = i//2  end = min(i,n-1) apply binary search.
    # apply binary search on subarray.
    start = i//2
    end = min(i,n-1)

    while start <= end:
        mid = start + (end - start) // 2

        if target ==  arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    n = len(arr)
    x = 40
    result = exponential_search(arr, x ,n)
    if result == -1:
        print ("Element not found in the array")
    else:
        print (f"Element is present at index {result}")








