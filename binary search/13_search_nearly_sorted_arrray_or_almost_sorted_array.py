def search_nearly_or_almost_sorted_array(arr,target):
    # nearly sorted array and almost sorted array kya hota h
 
    # ans 👀👀 apko jo array given h . usko just assume kero ki apne usko sort kar liya h .
 
    # ab us sort array me if koi element ith index par h -> to vo element (nearly sorted array and almost sorted array) unsorted array me
 
    # (ith) index , (i-1th) index and (i+1th) index par hoga. to isi logic ka use kar lena.
 
    # or ager vo element (ith) index , (i-1th) index and (i+1th) par nahi milta h to vo array
 
    # nearly sorted array and almost sorted array , nahi h usme binary search nahi lagega.
 
 
 
    start = 0
    end = len(arr)-1
 
    while start <= end:
        mid = start + (end - start) // 2
        if target == arr[mid]:
            return mid
        if target == arr[mid-1]:
            return mid-1
        if target == arr[mid+1]:
            return mid + 1
       
        if target < arr[mid]:
            # mid - 1 ko already cheack kar chuke h isiliye mid - 2 likha h.
            end = mid - 2
        else:
            # mid + 1 ko already cheack kar chuke h isiliye mid + 2 likha h.
            start = mid + 2
 
    return -1
   
if __name__ == "__main__":
    arr = [10, 3, 40, 20, 50, 80, 70]
    key = 40
 
    result = search_nearly_or_almost_sorted_array(arr,key)
    if result != -1:
        print(f"{key} found at index no. {result} in the array.")
    else:
        print(f"{key} not found in the array.")