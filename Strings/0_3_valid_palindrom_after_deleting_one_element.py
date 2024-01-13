def check_palindrome(remaning_string):
    start = 0
    end = len(remaning_string)-1

    while start <= end:
        if remaning_string[start] != remaning_string[end]:
           return False
        else:
            start += 1
            end -= 1
    return True

def valid_palindrome(s):
    # delete one character and check its palindrome or not.
    # so we use two pointer approch.
    i = 0
    j = len(s)-1

    while i <= j:
        if s[i] != s[j]:
            # agar both character not same to hi ham 1 character ko remove karege.
            return check_palindrome(s[i+1:j+1]) or check_palindrome(s[i:j])
        else:
            # both character are same just change the pointer. forword and prevoius.
            i += 1
            j -= 1
    return True

if __name__ == "__main__":
    s = "deeee"
    result = valid_palindrome(s)
    print(result)




