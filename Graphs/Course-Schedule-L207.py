'''
This is topological sort question. Topological sort can be used only on DAG.

Create DAG ( Directed Acyclic) graph using given course dependancies and then apply topological sorting.

prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
So add directed edge from bi to ai as bi should come first before ai.

'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = self.constructGraph(numCourses,prerequisites)
        
        #calculate indegree
        indegree = [ 0 for _ in range(numCourses)]
        for prereq in prerequisites:
            indegree[prereq[0]] += 1        
        
        return self.canFinish_toposort(graph,numCourses,indegree)
        
        
        
        
    
    def constructGraph(self,numCourses, prerequisites):
        
        graph = [[] for _ in range(numCourses)]
        
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        
        return graph
    
    def canFinish_toposort(self,graph,numCourses,indegree):
        ans = []
        q=deque()
        
        for index in range(numCourses):
            if indegree[index] == 0:
                q.append(index)
        
        
        while len(q):
            
            node = q.popleft()
            ans.append(node)
            
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
                
        
        return len(ans) == numCourses
        
        
        
        
