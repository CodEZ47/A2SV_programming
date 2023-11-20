class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:      
        uses = [0] * (n)
        room = 1
        meetings.sort()
        heap = []
        available_rooms = [i for i in range(n)]

        for meet in meetings:      
            while heap and heap[0][0] <= meet[0]:
                curr_end, freed_room = heapq.heappop(heap)
                heapq.heappush(available_rooms, freed_room)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(heap, (meet[1], room))
            else:
                t, room = heapq.heappop(heap)
                dur = meet[1]-meet[0]
                heapq.heappush(heap, (t + dur, room))

            uses[room] += 1

        maxi = max(uses)
        idx = uses.index(maxi)

        return idx