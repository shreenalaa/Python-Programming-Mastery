

n = int(input())
list = []
list = [int(item) for item in input().split()]

solution = [0]*n    # list of zeros

for i in range(n) :
    solution[list[i]-1] = i+1

print(" ".join(map(str,solution)))