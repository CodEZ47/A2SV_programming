class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        output = 0
        players.sort()
        trainers.sort()
        i = 0
        j = 0
        
        while i < len(players) and j < len(trainers):
            if trainers[j] >= players[i]:
                j += 1
                i += 1
                output += 1
            else:
                j += 1
        
        return output
            