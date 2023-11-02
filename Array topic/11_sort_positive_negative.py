# def sort_negative_positive(arr):
#     i = start = 0
#     end = len(arr) - 1

#     while i <= end:
#         if arr[i] < 0:
#             arr[i],arr[start] = arr[start],arr[i]
#             start += 1
#             i += 1
#         else:
#             arr[i],arr[end] = arr[end],arr[i]
#             end -= 1


def sort_negative_positive(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        if arr[start] < 0:
            # negative wala case.
            start += 1
        else:
            # positive wala case.
            arr[start],arr[end] = arr[end],arr[start]
            end -= 1

if __name__ == "__main__":
    arr = [-5,2,-1,4,2,-2,-4,3]
    # arr = [2,-5,0,0]
    sort_negative_positive(arr)
    print(arr)