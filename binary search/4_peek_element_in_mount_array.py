def get_peek(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = start + (end-start) // 2
        # check line no. 1
        if arr[mid] < arr[mid+1]:
            # go to right side
            start = mid + 1
        else:
            # peek element should be mid itself or lies in the line no. 2
            end = mid
    # you may retun start or end both are pointing to the same element or index.
    return end

if __name__ == "__main__":
    arr = [0,10,5,2]
    ans = get_peek(arr)
    print(f"Peek element {arr[ans]} found at index {ans}")




#Python #Algorithm #BinarySearch #CodingChallenge #Programming #TechTalk