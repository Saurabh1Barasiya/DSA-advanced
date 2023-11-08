def find_missing(arr):
    n = len(arr)
    i = 0
    while i < n:
        index = abs(arr[i])
        next_index = index - 1

        # if not  visited so, mark as visited. 
        if arr[next_index] > 0:
            arr[next_index] *= -1
        
        i+=1
    
    # print missing element
    j = 0
    while j < len(arr):
        if arr[j] > 0:
            print(j+1,end=" ")
        j+=1


if __name__ == "__main__":
    arr = [2,2,2,2,2]
    find_missing(arr)