
n = int(input())
list = []
list = [int(item) for item in input().split()]
d  ,ma , mi
for i in range (n):
      if (i!=0):
          mi = abs(list[i]-list[0])
          ma = mi
      else :

            mi = abs(list[1] - list[0])

            ma = mi
      for j in range (n):
           if(i!=j):
               d = abs(list[i]-list[j])
               if d<mi:
                      mi = d
                else if d > max :
                      ma = d


print (counter)