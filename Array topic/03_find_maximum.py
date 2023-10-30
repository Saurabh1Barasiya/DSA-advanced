# get maximum number in a array.

import sys

def get_maximum(arr):
    maxi = -sys.maxsize

    for element in arr:
        if maxi < element:
            maxi = element
    return maxi

if __name__ == "__main__":
    arr = [10,15,25,100,5,7,8,30]
    ans = get_maximum(arr)
    print(f"Maximum value in the array is {ans}")