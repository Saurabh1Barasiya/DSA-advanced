import math
def is_solution_possible(arr,h,mid):
    hours_count = 0
    for i in arr:
        hours_count += math.ceil(i / mid)

    if hours_count <= h:
        # agar hours_count less hai se (h). 
        # matlab sare banana end ho gaye h given time par.
        # solution possible h.
        return True
    else:
        # solution possible nahi h.
        return False
    

def ko_ko_eating(arr,h):
    # start = 1
    # end = max(arr)

    # ye bhi chalega....

    # or thoda search space ko kam karte h...
    # start = sum(arr) // h

    start = 1
    end = max(arr) 

    ans = -1
    while start <= end:
        mid = start + (end - start) // 2
        mid = max(mid,1)
        if is_solution_possible(arr,h,mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

if __name__ == "__main__":
    arr = [3,6,7,11]
    h = 8

    # arr = [30,11,23,4,20]
    # h = 5
    
    # arr = [30,11,23,4,20]
    # h = 6

    ans = ko_ko_eating(arr,h)
    print(ans)
