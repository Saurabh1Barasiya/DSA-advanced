def palindrome_count(new_arr,count):
    i = 0
    j = len(new_arr) - 1
    while i <= j:
        if new_arr[i] != new_arr[j]:
            break
        else:
            i += 1
            j -= 1
    else:
        count[0] = count[0] + 1


def get_substrinng_palindrome(s,n):
    string = list(s)
    count = [0]
    i = 0
    while i < n:
        j = i
        while j < n:
            new_arr = string[i:j+1]
            palindrome_count(new_arr,count)
            j += 1
        i += 1
    print("Total substring is",count)


if __name__ == "__main__":
    s = "abc"
    s = "aaa"
    n = len(s)
    result = get_substrinng_palindrome(s,n)
    # print(result)