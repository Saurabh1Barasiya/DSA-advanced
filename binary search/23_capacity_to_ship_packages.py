# Capacity To Ship Packages Within D Days.
def is_solution_possible(weights,capacity,total_days,N):
    # lets start with first day...
    day = 1
    load = 0
    for i in range(N):
        if load + weights[i] <= capacity:
            load += weights[i]
        else:
            day += 1
            if (day > total_days) or weights[i] > capacity:
                return False
            
            load = 0
            load += weights[i]
    return True


def load_shipped(weights,D,N):
    # lets make a search space.

    start = max(weights)
    end = sum(weights)

    ans = -1

    while start <= end:
        mid = start + (end-start) // 2
        if is_solution_possible(weights,mid,D,N):
            ans = mid
            end  = mid - 1
        else:
            start = mid + 1
    return ans

if __name__  == "__main__":
    weights = [1, 2, 1]
    weights = [9, 8, 10]
    weights = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    N = len(weights)
    result = load_shipped(weights,D,N)
    print(result)











