# search in nearly sorted array and sarch in almost sorted array.

def search_in_nearly_sorted_array(arr,target):
    start = 0 
    end = len(arr)-1

    while start <= end:
        mid = start + (end-start) // 2
        # ith , i-1th , i-2th 
        if target == arr[mid]:
            return mid

        if (mid-1 >= start) and (target == arr[mid-1]):
            return mid-1
        
        if (mid+1 <= end) and (target == arr[mid+1]):
            return mid+1

        if target < arr[mid]:
            end = mid - 2
        else:
            start = mid + 2

    return -1

if __name__ == "__main__":
    arr = [10, 3, 40, 20, 50, 80, 70]
    key = 70
    result = search_in_nearly_sorted_array(arr,key)
    if result != -1:
        print(f"Element {key} found at index no. {result} ")
    else:
        print("Element not found. ")



# 🚀 Excited to share my recent coding exploration! 🚀

# I've been working on an algorithm for searching in nearly sorted arrays. 🧐 This is a modified binary search to handle cases where the elements are almost sorted, allowing for efficient search operations.

# Check out the code on my GitHub repository: https://github.com/Saurabh1Barasiya/DSA-advanced


# 🕰️ Time Complexity: O(log n) - The algorithm maintains an efficient logarithmic time complexity due to its modified binary search nature.

# 💾 Space Complexity: O(1) - The algorithm uses a constant amount of extra space, making it memory-efficient regardless of the input size.

# Feel free to explore, contribute, or share your thoughts! 🤓 Let's learn and grow together. 🌱 #Coding #Algorithm #GitHub #Programming #Python #Dsa