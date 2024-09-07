
s={1,2,3,4,5,6,7}
print(s)

info={"Rupa",12,5.7,False}
print(info)

for i in info:
    print(i)

kirti=set()
print(type(kirti))
#___________________________
s1={1,4,6,3,23,45}
s2={8,4,6,7,12}

print(s1.union(s2)) # for adding set 1 and 2
print(s1.update(s2)) #for adding those element that are not present in the set
print(s1.intersection(s2)) #for element present in both sets
print(s1.symmetric_difference(s2)) #element which are not in both
print(s1.isdisjoint(s2)) #are both different and nothing in common
print(s1.issuperset(s2)) 
s1.add(69)
print(s1)
s1.remove(23)
print(s1)
s1.pop() #removes any random element
del s2   #removes the whole set
