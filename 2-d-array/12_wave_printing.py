def wave_printing(arr):
    row = len(arr)
    col = len(arr[0])

    # column wise print karna h.
    start_col = 0
    while start_col < col:
        if start_col % 2 == 0:
            # top to buttom
            i = 0
            while i < row:
                print(arr[i][start_col],end=" ")
                i += 1
        else:
            # buttom to top
            j = row-1
            while j >= 0:
               print(arr[j][start_col],end=" ")
               j -= 1
        start_col += 1

if __name__ == "__main__":
    arr = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
    ]
    wave_printing(arr)