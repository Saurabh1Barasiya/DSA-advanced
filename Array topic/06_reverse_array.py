# reverse array.

def reverse_array(arr):
    start_pointer = 0
    end_pointer = len(arr)-1

    while start_pointer < end_pointer:
        arr[start_pointer],arr[end_pointer] = arr[end_pointer],arr[start_pointer]
        start_pointer += 1
        end_pointer -= 1


if __name__ == "__main__":
    arr = [10,20,30,40,50,60,70,80]
    # arr = [10,20,30,40,50,60,70]
    
    reverse_array(arr)
    print(arr)
