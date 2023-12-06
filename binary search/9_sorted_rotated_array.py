def get_piviot(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end-start) // 2

        if start == end:
            return start

        if mid + 1 <= end and arr[mid] > arr[mid+1]:
            return mid
        if mid-1 >= start and arr[mid] < arr[mid-1]:
            return mid-1

        if arr[start] > arr[mid]:
            end = mid-1
        else:
            start = mid+1

def binary_search(arr,target,start,end):
    while start <= end:
        mid = start + (end-start) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
        


def search_rotated_array(arr,target):
    piviot = get_piviot(arr)
    # print("piviot is",piviot)

    if target >= arr[0] and target <= arr[piviot]:
        ans = binary_search(arr,target,0,piviot)
    else:
        ans = binary_search(arr,target,piviot+1,len(arr)-1)

    return ans


if __name__ == "__main__":
    arr = [4,5,6,7,0,1,2]
    target = 10
    result = search_rotated_array(arr,target)
    # print("result is",result)
    if result != -1:
        print(f"target {target} found in {result} index.")
    else:
        print(f"Target {target} not found")