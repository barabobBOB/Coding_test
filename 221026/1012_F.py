# 실패작

t = int(input())
result_list = []

def dfs(x):
    d_check = True
    for i in graph_list[x]:
        if d_check == False:
            dfs(i)

for _ in range(t):
    m, n, k = map(int, input().split())
    graph_list = [[]for _ in range(m)]
    d_check = [False for _ in range(m)]
    count = 0
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph_list[x].append(y)
        
    for i in range(n):
        dfs(i)
        count += 1
        
    result_list.append(count)
    
for i in result_list:
    print(i)