l=[1,2,3,2,1,3,4,5,5,3,2,4,3,2]
from collections import Counter
c=Counter(l)

for key,values in c.items():
  if value>1:
    return key


