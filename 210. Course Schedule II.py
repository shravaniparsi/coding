from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #edge cases
        if not numCourses and not prerequisites:
            return []
        
        # defining a dict
        graph = defaultdict(list)
        
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        
        result = []
        print(graph)
        
        # to keep track of visited edges
        visited = [0 for x in range(numCourses)]
        
        def dfs(i):
            # cycle detected
            if visited[i] == -1:
                return False
            # finished dfs for the node and no cycle detected
            if visited[i] == 1:
                return True
            # marking as visited
            visited[i] = -1
            
            for prereq in graph[i]:
                #cycle detected
                if not dfs(prereq):
                    return False
            # appending to the result
            result.append(i)
            # marking it as finished
            visited[i] = 1
            return True
        
        #iterating through courses and doing dfs
        
        for i in range(numCourses):
            # do the dfs and if it returns false that means it has a loop which means 
            # not possible to finish courses
            if not dfs(i):
                return []
        return result
        
        
                
                
                
            
        
        
        
