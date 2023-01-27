class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        s = 0
        e = len(people)-1
        boats = 0
        people.sort()
        
        while s <= e:
            if people[s] >= limit:
                boats += 1
                s += 1
                continue
            if people[e] >= limit:
                boats += 1
                e -= 1
                continue
            if people[s] + people[e] > limit:
                boats += 1
                e -= 1
                continue
            
            boats += 1
            s += 1
            e -= 1
        
        return boats