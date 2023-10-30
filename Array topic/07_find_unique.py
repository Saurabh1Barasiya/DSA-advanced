def find_unique(arr):
    for element in arr:
        if arr.count(element) == 1:
            print(element)

# def find_unique(arr):
#     ans = 0
#     for element in arr:
#         ans = ans ^ element
#     print(ans)


if __name__ == "__main__":
    arr = [1,2,4,2,1,3,6,5,5,6,4]
    arr = [2,10,11,5,6,2,5,6,10]
    find_unique(arr)
