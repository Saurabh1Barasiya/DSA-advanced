def transpose_2d_array(l1,l2):
    length = len(l1)

    for i in range(length):
        for j in range(len(l1[i])):
            l2[i][j] = l1[j][i]
    print(l2)

def print_array(arr):
    lenght = len(arr)
    for i in range(lenght):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print("")



if __name__ == "__main__":
    # l1 = [
    #         [4, 5, 3,],
    #         [7, 1, 8 ],
    #         [5, 6, 4,]
    #     ]
    l1 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    row = 3
    col = 3

    # for transpose we have to make a new 2-d array.

    l2 = [ [0 for j in range(col)] for i in range(row)]

    # print(l2)

    transpose_2d_array(l1,l2)
    print_array(l1)

    print("transpose the 2-d array")
    print_array(l2)
