# search space always 0 --------- dividend.
# formula = quotient * divisor = dividend.

def get_division(dividend,divisor):
    start = 0
    end = abs(dividend)
    ans = 0
    while start <= end:
        mid = start + (end - start) // 2

        if abs(dividend) == abs(mid * divisor):
            return mid
        elif abs(dividend) < abs(mid * divisor):
            end = mid - 1
        elif abs(dividend) > abs(mid * divisor):
            ans = mid
            start = mid + 1
        
    # now handle fraction part
    precision = 3
    steap = 0.1
    for _ in range(0,precision):
        while ans * abs(divisor) <= abs(dividend):
            ans += steap
        ans -= steap
        steap = steap / 10

    ans = round(ans,3)

    if (dividend < 0 and  divisor < 0) or (divisor > 0 and dividend > 0):
        return ans
    else:
        return -ans
    
if __name__ == "__main__":
    divisor = -3
    dividend = 10
    result = get_division(dividend,divisor)
    print(result)
