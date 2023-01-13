class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []
        for i in range(1, n+1):
            players.append(i)
        
        
        temp = []
        chk = 1
        ptr = 0
        
        if k == 1:
            return players[-1]
        
        
        while len(players) > 1:
            if ptr == len(players) - 1:
                if chk < k:
                    temp.append(players[ptr])
                    ptr = 0
                    chk += 1
                else:
                    ptr = 0
                    chk = 1
                players = temp
                temp = []
                continue
                
            if chk == k:
                ptr += 1
                chk = 1
                continue
            
            temp.append(players[ptr])
            ptr += 1
            chk += 1
        
        return players[0]
            
            
        
        
        