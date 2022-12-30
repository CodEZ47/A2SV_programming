class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        pow_lst = []
        num_dict = {}
        temp = 0
        foods_len = len(deliciousness)
        deliciousness.sort()
        
        for ind in range(22):
            pow_lst.append(pow(2,ind))
        
        for num in deliciousness:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        
        pairs = 0
        for num in pow_lst:
            for ind in range(foods_len):
                temp = num - deliciousness[ind]
                if temp < 0:
                    break
                if temp in num_dict and temp == deliciousness[ind] and num_dict[temp] > 1:
                    pairs += num_dict[temp]-1
                if temp in num_dict and temp != deliciousness[ind]:
                    pairs += num_dict[temp]
                
        pairs = pairs//2
        pairs = pairs % (pow(10,9) + 7)
            
        return pairs  
            