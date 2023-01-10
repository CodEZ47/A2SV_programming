class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        comm = 0
        temp = ""
        
        for line in source:
            idx = 0
            line_len = len(line)
            
            while idx < line_len:
                if idx < line_len - 1 and line[idx] == '/' and line[idx+1] == '/' and comm == 0:
                    idx = line_len
                elif idx < line_len - 1 and line[idx] == '/' and line[idx+1] == '*' and comm == 0:
                    comm = 1
                    idx += 1
                elif idx < line_len - 1 and line[idx] == '*' and line[idx+1] == '/' and comm == 1:
                    comm = 0
                    idx += 1
                elif comm == 0:
                    temp += line[idx]
                idx += 1

            if temp and comm == 0:
                answer.append(temp)
                temp = ""


        return answer