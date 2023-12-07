# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.


def divide(dividend, divisor):
        # quotient * divisor + reminder == dividend
        # quotient * divisor <= dividend

        # handling lower  and upper limit.
        if abs(divisor) == 1:
            dividend = dividend * divisor
            if dividend > 2**31 - 1:
               return 2 ** 31 - 1
            if dividend < -(2**31):
                return -2 ** 31
            return dividend

        new_dividend = abs(dividend)
        new_divisor = abs(divisor)

        start = 0
        end = new_dividend

        ans = 0

        while start <= end:
            mid = start + (end-start) // 2
            if new_dividend == mid * new_divisor:
                ans = mid
                break
            elif new_dividend < mid * new_divisor:
                end = mid - 1
            elif new_dividend > mid * new_divisor:
                ans = mid
                start = mid + 1
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            return ans
        else:
            return  -ans
        
if __name__ == "__main__":
   dividend = 11
   divisor = 2
   result = divide(dividend, divisor)
   print(result)



        
        
        