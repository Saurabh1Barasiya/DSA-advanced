# check wether element is present or not in the array.

def linear_search(arr,search_elem):
    for element in arr:
        if element == search_elem:
            return True
    return False

    
if __name__ == '__main__':
    arr = [2,9,6,7,4,12,15]
    search_elem = 6
    # search_elem = 16
    ans = linear_search(arr,search_elem)
    if ans:
        print(f"Element is present")
    else:
         print(f"Element is not present")


# TC => O(n).
# SC =>O(1).