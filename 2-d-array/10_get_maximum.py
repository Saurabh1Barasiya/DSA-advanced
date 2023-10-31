import sys

def get_maximum_element(arr):
    maxi = -sys.maxsize
    length = len(arr)
    for i in range(length):
        for j in range(len(arr[i])):
            if arr[i][j] > maxi:
                maxi = arr[i][j]
    print(f"maximum value is {maxi}")
    
if __name__ == "__main__":
    arr = [
        [5,4,6],
        [7,8,9],
        [1,10,5]
    ]

    get_maximum_element(arr)