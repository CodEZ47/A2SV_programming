class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        color = defaultdict(int)

        for i in range(len(recipes)):
            graph[recipes[i]] = ingredients[i]
        for i in range(len(ingredients)):
            for ing in ingredients[i]:
                if graph[ing]:
                    continue

        supplies = set(supplies)
        ans = []
        def dfs(node):
            nonlocal ans
            if color[node] == 2 or node in supplies:
                return True
            if color[node] == 1:
                return False
            if not graph[node] and node not in supplies:
                return False
            
            color[node] = 1
            val = True
            for neigh in graph[node]:
                comp = dfs(neigh)
                val = val and comp
            
            if val:
                ans.append(node)
                color[node] = 2
            
            return val
        
        for i in range(len(recipes)):
            dfs(recipes[i])

        return ans