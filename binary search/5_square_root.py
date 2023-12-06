def get_squre_root(n,precision):
    start = 0
    end = n
    target = n
    ans = -1

    # Binary search for integer part
    while start <= end:
        mid = start + (end - start) // 2
        if target == mid * mid:
            return mid
        elif target < mid * mid:
            end = mid - 1
        elif target > mid * mid:
            ans = mid
            start = mid + 1
        

    # Floating-point precision part
    step = 0.1

    for i in range(precision):
        while ans * ans <= n:
            ans = ans + step
        ans = ans - step
        step = step / 10

    return round(ans,3)

if __name__ == "__main__":
    n = int(input("Enter number for square root: "))
    precision = 3
    res = get_squre_root(n,precision)
    print(res)


