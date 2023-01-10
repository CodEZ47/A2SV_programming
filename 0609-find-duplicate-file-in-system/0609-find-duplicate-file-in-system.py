class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        paths_str = "*".join(paths)
        paths_str_len = len(paths_str)
        ind = 0
        content = ""
        root_path = ""
        file_path = "/"
        content_dict = defaultdict(list)
        final_arr = []
        # print(paths_str)
        
        while ind < paths_str_len:
            
            if paths_str[ind] == " ":
                ind += 1
                while paths_str[ind] != "(":
                    file_path += paths_str[ind]
                    ind += 1
                # print(file_path)
                continue
                    
            if paths_str[ind] == "(":
                ind += 1
                while paths_str[ind] != ")":
                    content += paths_str[ind]
                    ind += 1
                content_dict[content].append(root_path+file_path)
                content = ""
                continue
                
            if paths_str[ind] == ")":
                file_path = "/"
                ind += 1
                continue
                
            if paths_str[ind] == "*":
                root_path = ""
                ind += 1
                continue
                
            root_path += paths_str[ind]
            ind += 1
            # print(root_path, ind)
                
        temp = content_dict.values()
        for value in temp:
            if len(value) > 1:
                final_arr.append(value)
                
        # print(final_arr)
        return final_arr