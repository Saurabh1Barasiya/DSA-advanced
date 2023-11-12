def calc_Sum (arr,  n, brr, m) : 
    i = n-1
    j = m-1
    carry = 0
    ans = []
    
    while i >= 0 and j>=0:
        num = arr[i] + brr[j] + carry
        digit = num % 10
        carry = num // 10
        ans.append(digit)
        i -= 1
        j -= 1
    
    while i >= 0:
        # rest part of arr.
        num = arr[i] + 0 + carry
        digit = num % 10
        carry = num // 10
        ans.append(digit)
        i -= 1
    
    while j >= 0:
        # rest part of brr.
        num = 0 + brr[j] + carry
        digit = num % 10
        carry = num // 10
        ans.append(digit)
        j -= 1
        
    if carry:
        ans.append(carry)
        
    
    #remove 0 from original array.
    # ye loop i = 0 to N bhi chal jata.
    t = len(ans)-1
    while t >=0:
        if ans[-1] == 0:
            ans.pop()
        t-=1
    
    # get the originl answer.
    ans.reverse()
    # print(arr)
    return ''.join([str(elem) for elem in ans])
        
if __name__ == "__main__":
    arr = [9, 5, 4, 9] 
    brr = [2, 1, 4] 

    n = len(arr)
    m = len(brr)
    ans = calc_Sum (arr,  n, brr, m)
    print(ans)
