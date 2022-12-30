class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dict_player = {}
        dict_games = {}
        final_arr = [[],[]]
        
        for game in matches:
            if game[0] in dict_player:
                dict_player[game[0]] += 1
            else:
                dict_player[game[0]] = 1
            
            if game[1] in dict_player:
                dict_player[game[1]] -= 1
            else:
                dict_player[game[1]] = -1
            
            if game[0] in dict_games:
                dict_games[game[0]] += 1
            else:
                dict_games[game[0]] = 1
            
            if game[1] in dict_games:
                dict_games[game[1]] += 1
            else:
                dict_games[game[1]] = 1
        
        for key in dict_player:
            if dict_player[key] == dict_games[key]:
                final_arr[0].append(key)
            if dict_games[key] - dict_player[key] == 2:
                final_arr[1].append(key)
        
        final_arr[0].sort()
        final_arr[1].sort()
        
        # print(dict_player)
        # print(dict_games)
        print(final_arr)
        return final_arr