'''
def find_k_closest_element(arr,x,k):

    # time complexity is O(n log n).
    # space complexity is O(n).

    # fist calculate the diffrence.
    final_array = []
    diffrence = [(num,abs(num-x)) for num in arr]

    # first index par jo elelemt h (diffrence) ke  base par sort kar do.
    sorted_array = sorted(diffrence,key=lambda num:num[1])

    # first k elelemnt ko final array me store kar lo.
    for i in range(k):
        final_array.append(sorted_array[i][0])
    
    # ascending order me sort karke return kar do.
    final_array.sort()

    return final_array
'''


'''
    Time complexity : O(n).
    Space complexity : O(k).



    def find_k_closest_element(arr,x,k):

        # using two pointer approch.

        low = 0
        heigh = len(arr)-1

        while heigh - low >= k:
            # just minimize (shrink) to window size.
            if (x - arr[low]) > (arr[heigh] - x):
                low += 1
            else:
                heigh -= 1

        final_array = arr[low:heigh+1]
        return final_array

'''


# Now just solve using the concept of binary search.

def binary_search_for_lower_bound_or_closest_elelemnt(arr,target):
    start = 0
    end = len(arr) - 1

    # closest element nikalna h isiliye ans ko end se initilize kiya h.
    ans = end

    while start <= end:
        mid = start + (end-start) // 2
        
        if target <= arr[mid]:
            ans = mid
            end = mid - 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return ans


def find_k_closest_element(arr,x,k):
    heigh = binary_search_for_lower_bound_or_closest_elelemnt(arr,x)
    low = heigh - 1

    while k:
        # just maximize the widow to k.
        if low < 0:
            heigh += 1
        elif heigh >= len(arr):
            low -= 1
        elif x - arr[low] > arr[heigh] - x:
            heigh += 1
        else:
            low -= 1

        k -= 1

    final_array = arr[low+1:heigh]
    return final_array

# Time Complexity: O(log N + k)
# Space Complexity: O(k)
if __name__ == "__main__":
    # arr = [3,2,4,1,5]
    arr = [12,16,22,30,35,39,42,45,48,50,53,55,56]
    x = 35 
    k = 4
    result = find_k_closest_element(arr,x,k)
    print(result)



🚀 Excited to share a handy algorithm for finding k closest elements in a sorted array! 🚀

In this Python script, the binary_search_for_lower_bound_or_closest_element function performs a binary search to find the lower bound or closest element to the target. The find_k_closest_element function utilizes this and extends a window to find k closest elements efficiently.

Time Complexity: O(log N + k)
Space Complexity: O(k)

🔗 GitHub Repo: Link to Code

Feel free to explore, contribute, and share your thoughts! Let's dive into the world of algorithms and coding together! 💻✨ #CodingCommunity #Algorithms #Python #OpenSource