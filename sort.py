
n = int(input())
s = input()
lst = {}
s = s.lower()
for i in s :
    if i in lst :
        lst[i]+=1
    else :
        lst[i] = 1

if len(lst)==26 :
    print ("YES")
else :
    print("NO")