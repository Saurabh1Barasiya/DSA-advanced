def take_input(arr):
    row = 3
    col = 3
    for i in range(row):
        l = []
        for j in range(col):
            l.append(int(input()))
        arr.append(l)
    
def print_array(arr):
    lenght = len(arr)
    for i in range(lenght):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print("")

if __name__ == "__main__":
    arr = []
    take_input(arr)
    print_array(arr)