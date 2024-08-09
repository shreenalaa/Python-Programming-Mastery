s = int(input());
home = []
guest = []
for i in range(s):
    lst=[int(i) for i in input().split()]
    home.append(lst[0])
    guest.append(lst[1])
r=0
for i in range(s):
     for j in range (s):
         if home[i] == guest[j] :
               r=r+1


print (r)

# problem_link: https://codeforces.com/contest/268/problem/A
