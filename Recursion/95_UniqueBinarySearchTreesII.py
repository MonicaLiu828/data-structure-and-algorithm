# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # generate all tree nodes left from l right to r(include r) , return a list of all tree nodes
        def Tree(l,r):
            if l > r:
                return [None]
            else:
                new_Tree_collection = []
                # pick a root of plan to generated new tree
                for i in range(l,r+1):
                    # lefttree,return list of all lefttree nodes when root is i:
                    left_tree_collection = Tree(l,i-1)
                    # righttree,return list of all righttree nodes when root is i and r includes r
                    right_tree_collection = Tree(i+1,r)
                    #  make leftnode and rightnode connect with root
                    for eachleft in left_tree_collection:
                        for eachright in right_tree_collection:
                            newtree = TreeNode(i,eachleft,eachright)
                            new_Tree_collection.append(newtree)
            return new_Tree_collection
        return Tree(1,n)


