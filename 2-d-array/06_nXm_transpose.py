def transpose_2d_array(l1,l2,row,col):
    for i in range(row):
        for j in range(col):
            l2[i][j] = l1[j][i]
    

def print_array(arr):
    lenght = len(arr)
    for i in range(lenght):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print("")



if __name__ == "__main__":
    l1 = [
            [4, 5, 3, 9],
            [7, 1, 8 ,2],
            [5, 6, 4, 1]
        ]
    row = 3
    col = 4

    # for transpose we have to make a new 2-d array.

    l2 = [ [0 for j in range(row)] for i in range(col)]

    transpose_2d_array(l1,l2,col,row)

    print_array(l1)

    print("after transpose ")

    print_array(l2)


   