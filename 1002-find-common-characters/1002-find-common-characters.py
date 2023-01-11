class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        main_dict = defaultdict(int)
        temp_dict = defaultdict(int)
        dups = []
        
        for char in words[0]:
            main_dict[char] += 1
            
        for word in words:
            # print(word)
            for char in word:
                if char in main_dict and main_dict[char] > 0:
                    temp_dict[char] += 1
                    main_dict[char] -= 1
                else:
                    continue
                    
            main_dict = temp_dict.copy()
            temp_dict = defaultdict(int)
            
        for item in main_dict:
            temp = [item]*main_dict[item]
            dups = dups + temp
        
        return dups
        