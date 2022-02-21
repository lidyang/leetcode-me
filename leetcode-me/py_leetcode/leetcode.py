def minWindow(s, t):
    need = {}
    window = {}
    for a in t:need[a] = need.get(a,0)+1
    print("need")
    print(need)
    valid = 0
    start,left,right,l=0,0,0,100001
    while right < len(s):
        c = s[right]
        right=right+1
        if need.__contains__(c):
            window[c] = window.get(c,0)+1
            if window[c] == need[c]:
                valid=valid+1
        # print(right)
        while valid == len(need):
            if right-left < l:
                start = left
                l = right-left
            d = s[left]
            left=left+1
            if need.__contains__(d):
                if window[d] == need[d]:
                    valid = valid-1
                window[d] = window[d]-1
    
    print(l)
    print(start)
    if l == 100001:return ""
    else: return s[start:startl]


res = minWindow("ADOBECODEBANC","ABC")
print(res)


