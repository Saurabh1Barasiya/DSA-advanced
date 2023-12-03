def binary_search_in_2d(arr,target):
    total_column = len(arr[0])
    total_row = len(arr)

    start = 0
    end = total_row * total_column - 1

    while start <= end:
        mid = start + (end - start) // 2
        
        row_index = mid // total_column
        col_index = mid % total_column
        element = arr[row_index][col_index]

        if target == element:
            return [True,row_index,col_index]
        elif target < element:
            end = mid - 1
        elif target > element:
            start = mid + 1
    
    return -1

if __name__ == "__main__":
    arr = [
        [1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12]
    ]
    target = 12

    ans = binary_search_in_2d(arr,target)
    if ans == -1:
        print(f"{target} not found in the array")
    else:
        print(f"{target} found at row {ans[1]} and column {ans[2]}")






