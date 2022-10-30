from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # we will form tuples of type (time,username,website)
        webinfo = []
        
        for time,user,webpage in zip(timestamp,username,website):
            webinfo.append((time,user,webpage))
        
        # sort based on timestamps and usernames (if we have combination with equal count we need it to be based on username)
        webinfo.sort(key=lambda x:(x[0],x[1]))
        
        # we will form a dict with user as key and webpages he clicked as list of values
        # as we traverse webinfo which is sorted by timestamp
        # we get sequence of webpages visited by each user
        userpatterns = defaultdict(list)
        for _,user,webpage in webinfo:
            userpatterns[user].append(webpage)
        
        # now that we have sequence of webpages visited
        # we need to form all combinations of 3 and their count
        
        patternsofcount3 = defaultdict(int)
        for user in userpatterns:
            allpossiblecombinations = set(combinations(userpatterns[user], 3))
            # for each combination we store a count
            for combo in allpossiblecombinations:
                patternsofcount3[combo] += 1
        
        
        # sort based on count
        return max(sorted(patternsofcount3), key=patternsofcount3.get)
        
            
        
        
        
            
        
