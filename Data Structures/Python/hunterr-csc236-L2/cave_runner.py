from stack_that import stack_that
import sys

class cave_runner(object):
    #do I want to make a dictionary...???
    def __init__(self):
        self.traversed = stack_that()
        self.choices = []
        self.hat =  []
        self.size_x = 0
        self.size_y = 0
        self.row = 0
        self.col = 0
        self.found = 0
        self.new_pos = []
        
        #This stackoverflow helped me accomplish my for loop, before I was having
        #issues where iterating through a for loop could possibly delete information.
        #http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
        # wenda = raw_input("Please enter the name of the text file you wish to use:")
        with open('fourbysix.txt', "r") as waldos:
            for i in waldos:
                self.hat.append(i.strip())
        print self.hat
        
    # def set_locale(self):
    #     new_pos = [self.row, self.col]
    #     self.traversed.push([new_pos])
    #     print self.traversed.top()
        
    def check_locale(self,x,y):
        maze = self.hat
        #Base case  
        x = self.row
        y = self.col
        # if self.col > self.size_y or self.row > self.size_x:
        #     print("size error")
    
        if maze[x][y] == "T":
            self.my_precious()
    
        elif  maze[x][y] == "W":
            print("stuck on a wall?")
        elif maze[x][y] == 'M':
            maze[x][y] = 'V'
            if self.check_locale(self.row+1, self.col) == '.':  #North
                maze[x][y] = 'V'
            elif self.check_locale(self.row, self.col+1) == '.':  #East
                maze[x][y] = 'V' 
            elif self.check_locale(self.row-1, self.col) == '.':  #South
                maze[x][y] = 'V'  
            elif self.check_locale(self.row, self.col-1) == '.':  #West
                maze[x][y] = 'V'    
        elif maze[x][y] == '.':
            maze[x][y] = 'V'
            if self.check_locale(self.row+1, self.col) == '.':  #North
                maze[x][y] = 'V'
            elif self.check_locale(self.row, self.col+1) == '.':  #East
                maze[x][y] = 'V' 
            elif self.check_locale(self.row-1, self.col) == '.':  #South
                maze[x][y] = 'V'  
            elif self.check_locale(self.row, self.col-1) == '.':  #West
                maze[x][y] = 'V'    
            else:
                print('beg for mercy')
        else:
            self.found = 1
            for i in self.hat[0:]:
                get_out = open('solved.txt', 'a')
                get_out.write(i+"/n")
                get_out.close()
            print ("fin")
    
        # r = self.row+1
        # c = self.col
        # if self.hat[r][c] == '.':
        #     self.hat[r][c].write('O')
        #     self.step_N()
        # elif self.hat[r][c] == 'T':
        #     self.hat[r][c].write('C')
        #     self.my_precious()
        # else:
        #     r = self.row
        #     c = self.col+1
        #     if self.hat[r][c] == '.':
        #         self.hat[r][c].write('O')
        #         self.step_N()
        #     elif self.hat[r][c] == 'T':
        #         self.hat[r][c].write('C')
        #         self.my_precious()
        #     else:
        #         r = self.row-1
        #         c = self.col
        #         if self.hat[r][c] == '.':
        #             self.hat[r][c].write('O')
        #             self.step_N()
        #         elif self.hat[r][c] == 'T':
        #             self.hat[r][c].write('C')
        #             self.my_precious()
        #         else:
        #             r = self.row
        #             c = self.col-1
        #             if self.hat[r][c] == '.':
        #                 self.hat[r][c].write('O')
        #                 self.step_N()
        #             elif self.hat[r][c] == 'T':
        #                 self.hat[r][c].write('C')
        #                 self.my_precious()
        #             else:
        #                 print('tucansam!')
        #                 self.last_choice()
                        
                
        # E = self.row,    self.col+1
        # S = self.row-1,  self.col
        # W = self.row,    self.col-1

        # print("N:" + N)
        # print("E:" + E)
        # print("S:" + S)
        # print("W:" + W)
        # if N == ".":
        #     print(".")
        #     self.step_N()
        # if E == "T":
        #     self.my_precious()
        # elif E == ".":
        #     print(".")
        #     self.step_E()
        # elif E == "T":
        #     self.my_precious()
        # elif S == ".":
        #     print(".")
        #     self.step_S()
        # elif S == "T":
        #     self.my_precious()
        # elif W == ".":
        #     print(".")
        #     self.step_W()
        # elif W == "T":
        #     self.my_precious()        
        # else:
        #     self.last_choice()
            # sys.exit
            
    def last_choice(self):
        new_pos = []
        new_pos.append(self.traversed.pop())
        self.row = new_pos[0:]
        self.col = new_pos[:1]
        
    def find_entrance(self):
        for r in range(len(self.hat)):
            # print(r)
            for c in range(len(self.hat[r])):
                # print (c)
                if self.hat[r][c] == 'M':
                    self.row = r
                    self.col = c
                    self.choices.append([r,c])
        print self.choices

    # def step_N(self):
    #     r = self.row+1
    #     c = self.col
    #     self.choices.append([r,c])
        
    # def step_E(self):
    #     new_pos = self.row, self.col+1
    #     self[new_pos] = "M"
        
    # def step_S(self):
    #     new_pos = self.row-1, self.col
    #     self[new_pos] = "M"
        
    # def step_W(self):
    #     new_pos = self.col-1, self.col
    #     self[new_pos] = "M"
        
    def my_precious(self):
        new_pos = self.row, self.col
        self[new_pos] = "C"
        print("My Precious")

    # def the_visitor(self):
    #     #set what you've already visited to something else so you can tell.
    #     #maybe a V?
    #     #get self, set self to V
    #     position = self.row, self.col
    #     self.traversed.append([position])
    #     self[position] = "V"
    #     print self[position]

        