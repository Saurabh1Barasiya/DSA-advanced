def print_column_wise(arr):
    length = len(arr)

    print("Printing indexes")        
    for i in range(length):
        for j in range(length):
            print(f"{j}{i}",end=" ")
        print("")

    print("Printing array in column wise")        
    for i in range(length):
        for j in range(length):
            print(arr[j][i],end=" ")
        print("")

    print("Printing array in column wise")        
    for i in range(length):
        for j in range(len(arr[i])):
            print(arr[j][i],end=" ")
        print("")


if __name__ == "__main__":
    arr = [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]

    print_column_wise(arr)