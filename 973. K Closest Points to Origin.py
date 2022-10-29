class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # we are sorting based on dist and returning first k points
        
        #this gives us list of all distances from orgin for each (x,y)
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:k]
        
                    
        # this gives us o(NlogN) complexity        
    
        # To furthur increase efficiency we could do quick sort instead of inbult sort function
#         def dist(p):
#             return p[0]**2+p[1]**2
#         def partition(points, low, high):

#           # choose the rightmost element as pivot
#           pivot = dist(points[high])

#           # pointer for greater element
#           i = low - 1

#           # traverse through all elements
#           # compare each element with pivot
#           for j in range(low, high):
#             if dist(points[j]) <= pivot:
#               # if element smaller than pivot is found
#               # swap it with the greater element pointed by i
#               i = i + 1

#               # swapping element at i with element at j
#               (points[i], points[j]) = (points[j], points[i])

#           # swap the pivot element with the greater element specified by i
#           (points[i + 1], points[high]) = (points[high], points[i + 1])

#           # return the position from where partition is done
#           return i + 1

#         # function to perform quicksort
#         def quickSort(points, low, high):
#           if low < high:

#             # find pivot element such that
#             # element smaller than pivot are on the left
#             # element greater than pivot are on the right
#             pi = partition(points, low, high)

#             # recursive call on the left of pivot
#             quickSort(points, low, pi - 1)

#             # recursive call on the right of pivot
#             quickSort(points, pi + 1, high)
        
#         quickSort(points,0,len(points)-1)
        
#         return points[:k]
