def merge_two_array(arr,brr):
    n = len(arr)
    m = len(brr)

    i = j = 0
    ans = []
    while i < n and j < m:
        if arr[i] < brr[j]:
            ans.append(arr[i])
            i +=1
        else:
            ans.append(brr[j])
            j += 1

    while i < n:
        ans.append(arr[i])
        i += 1

    while j < m:
        ans.append(brr[j])
        j += 1

    return ans

if __name__ == "__main__":
    arr = [1,3,4,5]
    brr = [2,4,6,8]

    res = merge_two_array(arr,brr)
    print(res)