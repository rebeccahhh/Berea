#------------------------------------------------------------------------------#
# Write a function to calculate Body Mass Index: 
#
# BMI = (Weight/Height2) * 703. 
# (Weight is in pounds, height is in inches).
#
# Write an input loop that asks the user to enter a body weight and height.
# Add input validations to your program that prevents invalid inputs. 
# Write each validation as a separate function.
# Create a test suite to ensure your validation functions work properly. 
#------------------------------------------------------------------------------#

class bmi():
    def __init__(self):
        self.weight = 0
        self.height = 0
        
    def find_weight(self):
        user_weight = raw_input("Please enter your weight in pounds: ")
        try:
            int_weight = int(user_weight)
        except ValueError:
            print "I'm sorry, you may have entered this incorrectly, please try again."
            self.find_weight()
            
        if int_weight > 0 and int_weight < 500:
            self.weight = int_weight
        else:
            print "I'm sorry, you may have entered this incorrectly, please try again."
            self.find_weight()
        print self.weight
        return self.weight
       
 
    def find_height(self):
        user_height = raw_input("Please enter your height in inches: ")
        try:
            int_height = int(user_height)
        except ValueError:
            print "I'm sorry, you may have entered this incorrectly, please try again."
            self.find_height()

        if int_height > 0 and int_height < 110:
            self.height = int_height
        else:    
            print "I'm sorry, you may have entered this incorrectly, please try again."
            self.find_height()
        print self.height
        return self.height 
            
    def calcBMI(self):
        
        bmi = ((self.weight*703)//(self.height*self.height))
        print bmi
        
def main():
    user = bmi()
    user.find_weight()
    user.find_height()
    user.calcBMI()

main()