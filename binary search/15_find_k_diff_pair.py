'''
Approch 1.

# TC ---> O(n^2)
# SC ---> O(1)

def find_pair(arr,k):
    my_set = set()
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            diffrence = abs(arr[i] - arr[j])
            if diffrence == k:
                my_set.add((arr[i],arr[j]))
            j += 1
        i += 1
    return len(my_set)
'''


'''

# Approch 2. 
# Sliding window.
# 2 pointer.

def find_pair(arr,k):
    # if you apply two pointer, sliding window here so just sort the array.

    arr.sort()

    i = 0
    j = i + 1 
    while j < len(arr):
        diffrence = arr[j] - arr[i]
        if diffrence == k:  
           print(arr[i],arr[j])
           i += 1
           j += 1
        elif diffrence > k:
            # shrink the window.
            i += 1
        else:
            # grow the window.
            j += 1
        
        if i == j:
            j += 1
'''

def binary_search(arr,start,target):
    end = len(arr) - 1
    while start <= end:
        mid = start + (end-start) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def find_pair(arr,k):
    arr.sort()    # O(n log n).
    my_set = set()
    i = 0
    n = len(arr)
    while i < n:
        if binary_search(arr,i+1,arr[i]+k) != -1:
            my_set.add((arr[i],arr[i]+k))
        i += 1
    return len(my_set)

if __name__ == "__main__":
    arr = [3,1,4,1,5]
    k = 2
    ans = find_pair(arr,k)
    print(f"Total unique pair is {ans}")

 