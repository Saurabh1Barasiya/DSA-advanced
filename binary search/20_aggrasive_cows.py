def is_solution_possible(stalls,k,mid,N):
    # placed first cow...
    placed_cow = 1
    pos = stalls[0]

    # now placed remaning cows...
    for i in range(1,N):
        if pos + mid <= stalls[i]:
           placed_cow += 1
           pos = stalls[i]
        if placed_cow == k:
            return True
    return False

def place_cows(stalls,k,N):
    # make sure your array is sorted if not so please sort your array.
    stalls.sort()

    # make a search space.
    start = 0 
    end = max(stalls) - min(stalls)

    ans = -1

    while start <= end:
        mid = start + (end-start) // 2
        if is_solution_possible(stalls,k,mid,N):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans


if __name__ == "__main__":
    # stalls = [1,2,4,8,9]
    stalls =  [10,1,2,7,5]
    k=3
    N = len(stalls)
    result = place_cows(stalls,k,N)
    print(result)