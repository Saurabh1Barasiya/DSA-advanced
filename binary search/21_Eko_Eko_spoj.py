def is_solution_possible(trees,mid,m):
    sum_ = 0
    for tree in trees:
        if tree - mid <= 0:
            sum_ += 0
        else:
            sum_ += (tree - mid)
    if sum_ >= m:
        return True
    else:
        return False

def solve(trees,m,n):
    # make a search space.

    start = 0
    end = max(trees) # maximum value of a tree array.

    collected_wood = 0
    while start <= end:
        mid = start + (end - start) // 2
        if is_solution_possible(trees,mid,m):
            collected_wood = mid
            start = mid + 1
        else:
            end = mid - 1
    return collected_wood
    
if __name__ == "__main__":
    # n = 4
    # m = 7
    # arr = [20, 15, 10, 17]
    arr = [4 ,42 ,40, 26 ,46]
    n = 5 
    m = 20
    ans = solve(arr,m,n)
    print(ans)
