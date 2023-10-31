def row_wise_sum(arr):
    lenght = len(arr)
    for i in range(lenght):
        row_sum = 0
        for j in range(len(arr[i])):
            row_sum += arr[i][j]
        print(row_sum,end=" ")


if __name__ == "__main__":
    arr = [
        [1,2,3],
        [1,3,7],
        [4,6,8],
    ]

    row_wise_sum(arr)