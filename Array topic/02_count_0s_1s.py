def count_value(arr):
    zero_count = one_count = 0

    for element in arr:
        if element == 0:
            zero_count += 1
        if element == 1:
            one_count += 1
    return [zero_count,one_count]

if __name__ == "__main__":
    arr = [0,1,0,0,0,0,0,1,1,1,0,0,1,1]
    zeros,ones = count_value(arr)
    print(f"nubers of zeros is {zeros} and ones is {ones}")



# TC => O(n).
# SC =>O(1).