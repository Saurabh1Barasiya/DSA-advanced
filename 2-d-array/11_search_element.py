# linear search in 2-d array.

def linear_search(arr,key):
    length = len(arr)

    for i in range(length):
        for j in range(len(arr[i])):
            if arr[i][j] == key:
                print(f"yes key {arr[i][j]} found")
                break
    print(f"No key is not found")


if __name__ == "__main__":
    arr = [
        [5,4,6],
        [7,8,9],
        [1,10,5]
    ]
    key = 8
    linear_search(arr,key)