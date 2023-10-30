# print extreame array

def print_extrem(arr):
    start_pointer = 0
    end_pointer = len(arr)-1

    while start_pointer <= end_pointer:
        if start_pointer == end_pointer:
            print(arr[start_pointer],end=" ")
            return

        print(arr[start_pointer],end=" ")
        print(arr[end_pointer],end=" ")

        start_pointer += 1
        end_pointer -= 1

if __name__ == "__main__":
    arr = [10,20,30,40,50,60,70,80]
    # arr = [10,20,30,40,50,60,70]
    print_extrem(arr)