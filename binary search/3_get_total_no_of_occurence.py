def get_first_ocurrence(arr,target):
    start = 0
    end = len(arr) - 1
    ans = -1
    while start <= end:
        mid = start + (end - start) // 2
        if target == arr[mid]:
            ans = mid
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1 
        elif target < arr[mid]:
            end = mid - 1
    return ans

def get_last_ocurrence(arr,target):
    start = 0
    end = len(arr) - 1
    ans = -1
    while start <= end:
        mid = start + (end - start) // 2
        if target == arr[mid]:
            ans = mid
            start = mid + 1
        elif target > arr[mid]:
            start = mid + 1 
        elif target < arr[mid]:
            end = mid - 1
    return ans

def get_total_no_ocurrence(arr,target):
    first_ocurrence = get_first_ocurrence(arr,target)
    last_ocurrence = get_last_ocurrence(arr,target)


    if first_ocurrence == -1 or last_ocurrence == -1:
        return 0
    else:
        total_ocurrence = last_ocurrence - first_ocurrence + 1
        return total_ocurrence

if __name__ == "__main__":
    arr = [1,3,4,4,4,4,4,6,6,7,9]
    key = 4
    res = get_total_no_ocurrence(arr,key)
    print(f"total no of ocurrence of {key} is {res}")