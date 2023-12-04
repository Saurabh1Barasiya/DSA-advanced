def get_pivot(arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start +(end-start)//2

        if start == end:
            return start

        if mid-1 >= start and arr[mid] < arr[mid-1]:
            return mid-1

        if mid+1 <= end and arr[mid] > arr[mid+1]:
            return mid

        if arr[start] > arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1



if __name__ == "__main__":
    arr = [10,9]

    arr = [10,2,4,6,8,9]

    # arr = [9,10,2,4,6,8]



    

    ans = get_pivot(arr)
    print(arr[ans])










# arr = [9,10,2,4,6,8]