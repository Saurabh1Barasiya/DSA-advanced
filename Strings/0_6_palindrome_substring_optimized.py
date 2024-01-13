def check_palindrome(s,left,right):
    # i denote to left.
    # j denote to right.

    count = 0
    while (left >= 0 and right < len(s)) and (s[left] == s[right]):
        count += 1
        left -= 1
        right  += 1
    return count

def get_palindrome_substring(s,n):
    total_count = 0
    center = 0
    while center < n:
        # odd wala case i and j pointing to same place thats why we send (s,center,center)
        odd_ans = check_palindrome(s,center,center)
        total_count += odd_ans

        # even wala case i and j pointing to diffrent place thats why we send (s,center,center+1)
        even_ans = check_palindrome(s,center,center+1)
        total_count += even_ans

        center += 1
    return total_count

if __name__ == "__main__":
    s = "aaa"
    n = len(s)
    ans = get_palindrome_substring(s,n)
    print(ans)








