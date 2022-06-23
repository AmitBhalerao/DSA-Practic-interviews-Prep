'''
https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
Tarjans Algorithm concepts:

Discovery Time: This is the time when a node is visited 1st time while DFS traversal. For nodes A, B, C, .., and J in the DFS tree, Disc values are 1, 2, 3, .., 10. 

Low Time: In the DFS tree, Tree edges take us forward, from the ancestor node to one of its descendants. Back edges take us backward, from a descendant node to one of its ancestors. If we look at both Tree and Back edge together, then we can see that if we start traversal from one node, we may go down the tree via Tree edges and then go up via back edges. “Low Time” value of a node tells the topmost reachable ancestor (with minimum possible Disc value) via the subtree of that node. So for any node, a Low value is equal to its Disc value anyway (A node is the ancestor of itself). Then we look into its subtree and see if there is any node that can take us to any of its ancestors. If there are multiple back edges in the subtree that take us to different ancestors, then we take the one with the minimum Disc value (i.e. the topmost one). 

So basically if Low time of any node, is equal to topmost ancestor (min possible disc value) it will be able to reach using back-edge in DFS tree. 


'''

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = self.constructGraph(connections,n)
        return self.findCriticalEdge(n,graph)
    
    
    def findCriticalEdge(self,n,graph):
        
        discoveryTime=[-1 for _ in range(n)]
        lowTime = [-1 for _ in range(n)]
        time=[0]
        
        criticalEdges = []
        
        self.tarjansAlgo(0,time,-1,graph,discoveryTime,lowTime,criticalEdges)
        
        return criticalEdges
    
    def tarjansAlgo(self,currentVertex,time,currentParent,graph,discoveryTime,lowTime,criticalEdges):
        
        discoveryTime[currentVertex] = time[0]
        lowTime[currentVertex] = time[0]
        time[0]+=1
        
        for neigh in graph[currentVertex]:
            
            if neigh == currentParent:
                continue
            
            if discoveryTime[neigh] != -1:
                lowTime[currentVertex] = min(lowTime[currentVertex],discoveryTime[neigh])
                continue
            
            self.tarjansAlgo(neigh,time,currentVertex,graph,discoveryTime,lowTime,criticalEdges)

            # This below two lines are important for the algorithm to work. Remember them OR try to understand more
            lowTime[currentVertex] = min(lowTime[currentVertex],lowTime[neigh])
            
            #below condition gives correct answers for all testcases. But if lowTimes of currentVertex and nei are different means that edge is critical, so far that's the understanding. But may be for that all discovery time and low time needs to be calculated first.
            if discoveryTime[currentVertex] < lowTime[neigh]:
                criticalEdges.append([currentVertex,neigh])
        
        return criticalEdges
    
    
    
    def constructGraph(self,connections,n):
        
        graph=[[] for _ in range(n)]
        
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        return graph
        
        
