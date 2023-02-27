class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        l = 0
        fruits_dict = defaultdict(int)
        
        for i in range(len(fruits)):
            fruits_dict[fruits[i]] += 1
            
            while len(fruits_dict) > 2:
                fruits_dict[fruits[l]] -= 1
                l += 1
                
                if not fruits_dict[fruits[l-1]]:
                    fruits_dict.pop(fruits[l-1])
            
            max_fruits = max(max_fruits, sum(fruits_dict.values()))
        
        return max_fruits