# get maximum number in a array.

import sys

def get_manimum(arr):
    mini = sys.maxsize

    for element in arr:
        if mini > element:
            mini = element
    return mini

if __name__ == "__main__":
    arr = [10,15,25,100,5,7,8,30]
    ans = get_manimum(arr)
    print(f"Minimmum value in the array is {ans}")