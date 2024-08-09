
s = input()
a = 97    # for first character only
counter = 0
for i in range (len(s)):

    sub = abs((ord (s[i]))-a)
    if sub<=13:
        counter +=sub
        a = ord(s[i])   # for next char
    else :
       counter+=(abs(26-sub))  # rotate 
       a = ord(s[i])
print(counter)

