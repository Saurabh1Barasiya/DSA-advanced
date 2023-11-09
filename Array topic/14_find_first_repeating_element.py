def first_repeat_element(arr):
    i = 0
    n = len(arr)
    while i < n-1:
        j = i+1
        while j < n:
            if arr[i] == arr[j]:
                return i+1
            j+=1
        i+=1
    return -1

if __name__ == "__main__":
    arr = [1,5,3,4,3,5]
    ans = first_repeat_element(arr)
    print(f"First repeating element index {ans} and element is {arr[ans-1]}")
