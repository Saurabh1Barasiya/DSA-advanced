def removeOccurrences(s, part):
    while s.find(part) != -1:
        s = s.replace(part,"",1)
    return s
    
if __name__ == "__main__":
    s = "daabcbaabcbc"
    part = "abc"
    final_ans = removeOccurrences(s, part)
    print(final_ans)
