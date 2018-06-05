l1 = [int(x) for x in input().split()]

n,k = l1[0], l1[1]

l = [int(x) for x in input().split()]

s=0

for i in range(k):
   s = s + l[i]
print(s)