class stack_that():
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1]
    
    def row(self):
        self.items.append(object)
