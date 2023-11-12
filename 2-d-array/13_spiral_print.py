def spiral_printing(arr):
    row = len(arr)
    col = len(arr[0])

    # row wise print karna h.
    start_row = 0
    while start_row < row:
        if start_row % 2 == 0:
            # left to right
            i = 0
            while i < col:
                print(arr[start_row][i],end=" ")
                i += 1
        else:
            # right to left
            j = col-1
            while j >= 0:
               print(arr[start_row][j],end=" ")
               j -= 1
               
        start_row += 1

if __name__ == "__main__":
    arr = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
    ]
    spiral_printing(arr)