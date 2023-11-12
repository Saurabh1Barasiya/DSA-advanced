# we want output as an array format.
def factorial(N):
        #code here
        ans = []
        ans.append(1)
        i = 2
        carray = 0
        while i<=N:
            j = 0
            
            while j < len(ans):
                x = ans[j] * i + carray
                ans[j] = x % 10
                carray = x // 10
                j+=1
                
            if carray:
                ans.append(carray)
            carray = 0
                
            i+=1
                
            # reverse the array to original ans
        ans.reverse()
        return ans

if __name__ == "__main__":
    ans = factorial(5)
    print(ans)
