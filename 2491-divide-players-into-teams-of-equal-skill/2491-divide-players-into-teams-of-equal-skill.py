class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s = 0
        e = len(skill)-1
        chem = skill[s] + skill[e]
        tot_skill = 0
        
        while s < e:
            if skill[s] + skill[e] != chem:
                return -1
            tot_skill  += (skill[s]*skill[e])
            s += 1
            e -= 1
        
        return tot_skill