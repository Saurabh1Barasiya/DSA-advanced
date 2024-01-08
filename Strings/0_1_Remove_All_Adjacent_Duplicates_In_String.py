def remove_duplicate_adjacent(s):
    ans = []
    N = len(s)
    for i in range(N):
        if len(ans) > 0 and ans[-1] == s[i]:
            ans.pop()
        else:
            ans.append(s[i])
    return "".join(ans)

if __name__ == "__main__":
    s = "abbaca"
    s = "azxxzy"
    result = remove_duplicate_adjacent(s)
    print(result)