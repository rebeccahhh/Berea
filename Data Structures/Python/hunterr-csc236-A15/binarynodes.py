class binarynodes():
    def __init__(self, value = '', left = None, right = None):

        self.value = value
        self.right = right
        self.left = left
        
    def set_value(self, value):
        self.value = value
        
    # def subtree_insert(self,root,item):
    #     #From page 234 of Data Structures using Python and C++ by David M. Reed and John Zelle
    #     if root is None:
    #         return self.set_value(item)
    #     if item == root.item:
    #         print("help me Obi-Wan Kanobi, You're my only hope.."
    #     if item < root.value:
    #         root.left = self.subtree_insert(root.left, item)
    #     else:
    #         root.right = self.subtree_insert(root.right, item)