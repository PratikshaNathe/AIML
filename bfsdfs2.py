from collections import deque
import time

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['G'],
    'F':['G'],
    'G':[]
}

def bfs(start,goal):
    queue=deque([(start,[start])])
    visited=[]
    start_time=time.time()
    while queue:
        node,path=queue.popleft()
        if node is not visited:
            visited.append(node)
        if node==goal:
            return path,visited,time.time()-start_time

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour,path+[neighbour]))
    return None,visited,time.time()-start_time


def dfs(start,goal):
    stack=[(start,[start])]
    visited=[]
    start_time=time.time()
    while stack:
        node,path=stack.pop()
        if node is not visited:
            visited.append(node)
        if node==goal:
            return path,visited,time.time()-start_time

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour,path+[neighbour]))
    return None,visited,time.time()-start_time



path,visited,t=bfs('A','G')

print("BFS Path : ",path)
print("path length : ",len(path)-1 if path else 0)
print("Nodes explore : ",len(visited))
print("execution time : ",t)


path,visited,t=dfs('A','G')

print("DFS Path : ",path)
print("path length : ",len(path)-1 if path else 0)
print("Nodes explore : ",len(visited))
print("execution time : ",t)
            
