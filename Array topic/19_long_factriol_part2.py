def factriol(N):
    fact = 1
    for i in  range(1,N+1):
        fact *= i
    
    string_array = list(str(fact))
    final_array = list(map(lambda x:int(x),string_array))
    return final_array

if __name__ == "__main__":
    N = 5
    res = factriol(N)
    print(res)