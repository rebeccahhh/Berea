from digit_letter import digit_letter
import sys

class dr_seuss(object):
    def __init__(self):
        
        self.once_ler = []
        self.the_lorax()
        
    def the_lorax(self):
        green_eggs = raw_input("please enter a digit 1-9:")
        and_ham = digit_letter()
        and_ham.digits_to_letters_1(green_eggs)
        y = and_ham.final_list

        if y == ['0']:
            #print ('stop your damn nonsense')
            return self.once_ler
        else:
            for i in y:
                self.once_ler.append(str(i) + "X")
            self.the_lorax()
                
        print self.once_ler