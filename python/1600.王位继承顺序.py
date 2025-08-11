#
# @lc app=leetcode.cn id=1600 lang=python3
#
# [1600] 王位继承顺序
#

# @lc code=start
class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.death = False
        self.chidren = None
        self.bro = None
        
    def addchilren(self, name):
        if self.chidren == None:
            self.chidren = Node(name)
            return self.chidren
        else:
            bro = self.chidren
            while bro.bro:
                bro = bro.bro
            bro.bro = Node(name)
            return bro.bro
    
    # def __str__(self) -> str:
    #     return f"name: {self.name}, dead: {self.death}"

class ThroneInheritance:
    '''
    题目唬人的东西
    没有含金量的东西
    我写的兄弟子孙树，用儿子树也无所谓
    重点就是怎么遍历和怎么快速修改某一节点的信息
    那你存下来就行了呗，反正都已经是一个对象了，note（dict）里存的也是地址
    '''
    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.note = {kingName: self.root}
        

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.note[parentName]
        child = parent.addchilren(childName)
        self.note[childName] = child

    def death(self, name: str) -> None:
        self.note[name].death = True

    def getInheritanceOrder(self) -> List[str]:
        result = []
        def dfs(node, namelist):
            if node.death == False:
                namelist.append(node.name)
            
            if node.chidren:
                dfs(node.chidren, namelist)
            if node.bro:
                dfs(node.bro, namelist)
        dfs(self.root, result)
        return result
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
# @lc code=end

