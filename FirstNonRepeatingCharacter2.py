# Given a string s consisting of lowercase letters, for each position i in the string (0 ≤ i < n), find the first non-repeating character in the prefix s[0..i]. If no such character exists, use '#'.

from collections import deque

def nonRepeating(s):
    charCount = {}
    queue = deque()
    output = []

    for i in s:
        charCount[i] = charCount.get(i, 0) +1
        queue.append(i)
        while queue and charCount[queue[0]] >1:
            queue.popleft()

        if queue: # queue not empty
            output.append(queue[0])
        else:
            output.append('#')

    return "".join(output)

s1 = "aabc"
print(nonRepeating(s1))

# time complexity : O(N^2)