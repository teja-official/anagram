import sys
f = open(sys.argv[1], 'r')
l1 = [j for i in f.readlines() for j in i.split()]
l2 = []
for i in l1:
    j = i.strip('.').strip(',')
    if len(j)==4:
        l2.append(j)
l2 = list(set(l2))
def rotate(input,d): 
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    return Lsecond + Lfirst

anagrams = []
import itertools
for a, b in itertools.combinations(l2, 2):
    if set(list(a.lower()))==set(list(b.lower())):
        anagrams.extend([a, b])
print(",".join(sorted(list(set(anagrams)), key=str.lower)))
