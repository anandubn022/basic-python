# Given a string s consisting of lowercase letters, for each position i in the string (0 ≤ i < n), find the first non-repeating character in the prefix s[0..i]. If no such character exists, use '#'.

def nonRepeating(s):
    l = []
    o = []
    for i in s:
        if i not in l:
            l.append(i)
            o.append(l[0])
        else:
            l = []
            o.append('#')

    return "".join(o)
        
        

s1 = "aabc"
print(nonRepeating(s1))

# time complexity : O(N^2)