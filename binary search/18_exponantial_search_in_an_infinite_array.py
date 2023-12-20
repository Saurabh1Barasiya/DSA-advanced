def binary_search(start,end,target): 
    while start <= end:
        mid = start + (end - start) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def find_sub_array(arr, target):
    if target == arr[0]:
        return 0
    
    prev_ = 0
    next_ = 1

    while next_ <= len(arr) and arr[next_] <= target:
        prev_ = next_
        next_ = next_ * 2

    # apply binary search.
    return binary_search(prev_,min(next_,len(arr)-1),target)


if __name__ == "__main__":
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    target = 170
    # Function call
    ans = find_sub_array(arr, target)
    if ans == -1:
        print("Element not found")
    else:
        print("Element found at index", ans)