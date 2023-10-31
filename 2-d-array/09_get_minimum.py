import sys

def get_minimum_element(arr):
    mini = sys.maxsize
    length = len(arr)
    for i in range(length):
        for j in range(len(arr[i])):
            if arr[i][j] < mini:
                mini = arr[i][j]
    print(f"minimum value is {mini}")
    
if __name__ == "__main__":
    arr = [
        [5,4,6],
        [7,8,9],
        [1,2,5]
    ]

    get_minimum_element(arr)