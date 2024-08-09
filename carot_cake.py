

n = int(input())
list = []
list = [int(item) for item in input().split()]

sum = 0
for i in range(n):
   sum+=list[i]

sum = sum/2
list.sort(reverse=True)      # sorts the list in the descending order.
x = len(list)
counter = 0
result = 0
for i in range (x):   # take larger value
      result += list[i]
      counter+=1
      if result > sum:
         break


print(counter)