class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal = 0
        min_sal = 10000000
        sum_tot = 0
        
        for amnt in salary:
            if amnt > max_sal:
                max_sal = amnt
            if amnt < min_sal:
                min_sal = amnt
                
            sum_tot += amnt
        
        sum_tot -= max_sal + min_sal
        avg = sum_tot/(len(salary)-2)
        
        print(avg)
        return avg