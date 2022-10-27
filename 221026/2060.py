from collections import deque

n = int(input())
k = int(input())

graph_list = [[] for _ in range(n + 1)]
d_check = [False for _ in range(n + 1)]

for _ in range(k):
    com1, com2 = map(int, input().split())
    graph_list[com1].append(com2)
    graph_list[com2].append(com1)

d_check = [False for _ in range(n + 1)]  

def dfs(x, sum):
    d_check[x] = True
    sum += 1
    for j in graph_list[x]:
        if d_check[j] == False:
            sum = dfs(j, sum)
    return sum

print(dfs(1, 0) - 1)