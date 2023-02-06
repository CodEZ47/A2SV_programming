class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        seek = 0
        
        curr = chars[0]
        ctr = 0
        
        if len(chars) == 1:
            return 1
        
        while seek < len(chars):
            if chars[seek] == curr:
                ctr += 1
                seek += 1
                continue
            if chars[seek] != curr:
                if ctr == 1:
                    chars[l] = curr
                    l += 1
                else:
                    chars[l] = curr
                    l += 1
                    ctr = str(ctr)
                    ctr = list(ctr)
                    print(ctr)
                    ctr.reverse()
                    while ctr:
                        chars[l] = ctr.pop()
                        l += 1
                curr = chars[seek]
                ctr = 1
            seek += 1
            
        if ctr == 1:
            chars[l] = curr
            l += 1
        else:
            chars[l] = curr
            l += 1
            ctr = str(ctr)
            ctr = list(ctr)
            print(ctr)
            ctr.reverse()
            while ctr:
                chars[l] = ctr.pop()
                l += 1
        # print(chars)
        
        return l
                    