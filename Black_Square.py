
n,t,k,d = [int(i) for i in input().split()]

x =(int) ((n + k - 1) / k  )

t1 = 0

t2 = d

for i  in  range (x):

    if t1 <= t2 :
       t1 += t
    else :
      t2 += t

if max(t1, t2) < x * t :
        print("YES")
else :
       print("NO")
