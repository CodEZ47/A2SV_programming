class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingdom = defaultdict(list)
        self.kingName = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.kingdom[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(name):
            if name not in self.dead:
                order.append(name)

            for suc in self.kingdom[name]:
                dfs(suc)
        
        dfs(self.kingName)
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()