def get_square_root(target):
    start = 0
    end = target
    ans = -1

    while start <= end:
        mid = start + (end - start) // 2
        if target == mid * mid:
            return mid
        elif target < mid * mid:
            end = mid - 1
        elif target > mid*mid:
            ans = mid
            start = mid + 1
    return ans

if __name__ == "__main__":
    number = 10
    result = get_square_root(number)
    print(result)