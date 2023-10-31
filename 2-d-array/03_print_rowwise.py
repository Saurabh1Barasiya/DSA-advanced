def print_row_wise(arr):
    length = len(arr)

    print("Printing indexes")        
    for i in range(length):
        for j in range(length):
            print(f"{i}{j}",end=" ")
        print("")

    print("Printing array in row wise")        
    for i in range(length):
        for j in range(length):
            print(arr[i][j],end=" ")
        print("")

    print("Printing array in row wise")        
    for i in range(length):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print("")

if __name__ == "__main__":
    arr = [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]

    print_row_wise(arr)