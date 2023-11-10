# def get_common_elements(ar1,ar2,ar3):
#     l = []
#     for element in ar1:
#         if element in ar2 and element in ar3:
#             l.append(element)
#     return l



def get_common_elements(ar1,ar2,ar3):
    i = j = k = 0
    n1 = len(ar1)
    n2 = len(ar2)
    n3 = len(ar3)
    common = set()

    while i < n1 and j < n2 and k < n3:
        if ar1[i] == ar2[j] and ar2[j] == ar3[k]:
            common.add(ar1[i])
            i+=1
            j+=1
            k+=1
        elif ar1[i] < ar2[j]:
            i += 1
        elif ar2[j] < ar3[k]:
            j += 1
        else:
            k += 1
    return common

if __name__ == "__main__":
    ar1 = [1, 5, 10, 20, 40, 80] 
    ar2 = [6, 7, 20, 80, 100] 
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120] 

    ans = get_common_elements(ar1,ar2,ar3)
    print(ans)


# Time and Space Complexity:
# Time Complexity: O(n * m * p) where n, m, and p are the lengths of ar1, ar2, and ar3 respectively.
# Space Complexity: O(min(n, m, p))
