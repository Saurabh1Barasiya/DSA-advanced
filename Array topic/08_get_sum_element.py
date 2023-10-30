# def get_two_pair(arr,sum_):
#     i = 0
#     while i  < len(arr):
#         j = i+1 
#         while j < len(arr):
#             if arr[i] + arr[j] == sum_:
#                 print([arr[i],arr[j]])
#             j += 1
#         i += 1


# def get_three_pair(arr,sum_):
#     i = 0
#     while i  < len(arr):
#         j = i+1 
#         while j < len(arr):
#             k = j+1
#             while k < len(arr):
#                 if arr[i] + arr[j] + arr[k] == sum_:
#                     print([arr[i],arr[j],arr[k]])
#                 k += 1
#             j += 1
#         i += 1


def get_four_pair(arr,sum_):
    i = 0
    while i  < len(arr):
        j = i+1 
        while j < len(arr):
            k = j+1
            while k < len(arr):
                p = k + 1
                while p < len(arr):
                    if arr[i] + arr[j] + arr[k] + arr[p]== sum_:
                        print([arr[i],arr[j],arr[k],arr[p]])
                    p+=1
                k += 1
            j += 1
        i += 1


if __name__ == "__main__":
    # arr = [1,3,5,7,2,4,6]
    # get_two_pair(arr,9)

    # arr = [10,20,30,40,50]
    # get_three_pair(arr,80)

    arr = [1,3,5,7,2,4,6,9,11]
    
    get_four_pair(arr,13)
