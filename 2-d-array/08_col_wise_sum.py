def col_wise_sum(arr):
    lenght = len(arr)
    for i in range(lenght):
        col_sum = 0
        for j in range(len(arr[i])):
            col_sum += arr[j][i]
        print(col_sum,end=" ")


if __name__ == "__main__":
    arr = [
        [1,2,3],
        [5,1,2],
        [4,6,8],
    ]

    col_wise_sum(arr)