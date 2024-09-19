#counter function

from collections import Counter

l = [1, 2, 3, 2, 1, 3, 4, 5, 5, 3, 2, 4, 3, 2]
c = Counter(l)

# Iterate through the Counter object to find elements with more than one occurrence
for key, value in c.items():
    if value > 1:
        print(f"Element {key} occurs {value} times.")



