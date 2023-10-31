def print_array(arr):
    lenght = len(arr)
    
    # printing the array.

    # for row in range(lenght):
    #     for col in range(lenght):
    #         print(arr[row][col],end=" ")
    #     print("")

    # for i in range(lenght):
    #     for j in range(lenght):
    #         print(arr[i][j],end=" ")
    #     print("")


    # for i in range(lenght):
    #     print(arr[i])

    for i in range(lenght):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print("")

if __name__ == "__main__":
    arr = [[1,2,3],[4,5],[7,8,9]]
   

    # print(arr[0])
    # print(arr[1])
    # print(arr[2])

    print_array(arr)