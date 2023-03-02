class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        temp = []

        print(arr)

        for p in arr:
            if p == "" or p == ".":
                continue
            if p == ".." and temp:
                temp.pop()
            elif p != "..":
                temp.append(p)
        
        print(temp)

        temp = "/".join(temp)
        temp = "/" + temp
        return temp