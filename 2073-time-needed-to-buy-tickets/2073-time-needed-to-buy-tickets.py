class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            if i < k:
                if tickets[i] > tickets[k]:
                    time += tickets[k]
                else:
                    time += tickets[i]
            if i > k:
                if tickets[i] >= tickets[k]-1:
                    time += tickets[k]-1
                else:
                    time += tickets[i]
        time += tickets[k]
        return time