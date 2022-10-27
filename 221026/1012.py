
def dfs(x, y):
    visited[x][y] = True
    # 상, 하, 좌, 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if graph_list[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)
                
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph_list = [[0] * n for _ in range(m)]
    print(graph_list)
    visited = [[False] * n for _ in range(m)]
    
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph_list[x][y] = 1
        print(graph_list)
    
    for i in range(m):
        for j in range(n):
            if graph_list[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    print(count)