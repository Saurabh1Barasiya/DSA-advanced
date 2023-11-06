'''
def remove_duplicate(arr, n):
    # First, let's sort the array in ascending order.
    arr.sort()
    
    # Initialize the index to traverse the array.
    i = 0
    
    # Iterate through the array until the second-to-last next_index.
    while i < n - 1:
        # Check if the current next_index is the same as the next one.
        if arr[i] == arr[i + 1]:
            # If a duplicate is found, return it.
            return arr[i]
        i += 1
    
    # If no duplicate is found, return False.
    return False
'''


def remove_duplicate(nums):
    i = 0
    ans = -1
    while i < len(arr):
        # get the next_index as index
        next_index = abs(nums[i])
        

        # if element is negative so ans is next_index itself.
        if nums[next_index] < 0:
            ans = next_index
            break

        nums[next_index] *= -1

        i+=1
    return ans




if __name__ == "__main__":
    # Example usage:
    arr = [5,1,5,4,2,3]
    n = len(arr)
    
    # Call the function and print the result.
    ans = remove_duplicate(arr, n)
    print(ans)
