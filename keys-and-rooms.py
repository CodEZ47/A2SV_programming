class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        visited = set()
        queue.append(0)

        while queue:
            temp = deque()

            while queue:
                key = queue.popleft()
                
                
                if key not in visited:
                    for k in rooms[key]:
                        temp.append(k)
                visited.add(key)
            queue = temp.copy()
        
        
        if len(visited) == len(rooms):
            return True
        
        return False