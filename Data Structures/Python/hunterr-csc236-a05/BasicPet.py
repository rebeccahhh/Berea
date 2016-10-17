class BasicPet:
    '''A basic pet without specific characteristics. Just 3 basic needs. 
    Food/Water, Activity, and love.
    '''
   
    def __init__(self, food = 0, metabolism = 0, love = 0, neglect = 5):
        self.food = food
        self.metabolism = metabolism
        self.love = love
        self.neglect = neglect

        
    def feedMe(self):
        '''Adds one to the food attribute.'''
        self.food = self.food + 1
    
    
    def loveMe(self):
        '''Adds one to the love attribute.'''
        self.love = self.love + 1
    
    
    def walkMe(self):
        '''Adds one to the metabolism attribute.'''
        self.metabolism = self.metabolism + 1
    
    
    def neglectMe(self):
        '''subtracts one from the neglect attribute.'''
        self.neglect = self.neglect - 1
    
###############################################################################    
#    def getPetStats(self):
#        '''returns attributes, but was not utilised in the current project.'''
#        return self.food and self.metabolism and self.love and self.neglect
################################################################################  
        
    def checkPet(self):
        '''outputs attribute levels so the user can view them.'''
        print "Satiation: %s" % self.food
        print "Metabolism: %s" % self.metabolism
        print "Happiness: %s" % self.love
        print "Neglect level: %s" % self.neglect
        #return self.food and self.metabolism and self.love and self.neglect
    
    