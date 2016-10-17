class digit_letter(object):
    def __init__(self):
        print("Digit Conversion:")
        self.final_list = []
        
    def digits_to_letters_1(self, digit):
        digit_ = digit
        if digit_ == "1":
            self.final_list.append(" ")
        elif digit_ == "2":
            self.final_list.append("A")
            self.final_list.append("B")
            self.final_list.append("C")
            self.final_list.append("")

        elif digit_ == "3":
            self.final_list.append("D")
            self.final_list.append("E")
            self.final_list.append("F")
            self.final_list.append("")
            
        elif digit_ == "4":
            self.final_list.append("G")
            self.final_list.append("H")
            self.final_list.append("I")
            self.final_list.append("")
        
        elif digit_ == "5":
            self.final_list.append("J")
            self.final_list.append("K")
            self.final_list.append("L")
            self.final_list.append("")
            
        elif digit_ == "6":
            self.final_list.append("M")
            self.final_list.append("N")
            self.final_list.append("O")
            self.final_list.append("")
            
        elif digit_ == "7":
            self.final_list.append("P")
            self.final_list.append("Q")
            self.final_list.append("R")
            self.final_list.append("S")
            
        elif digit_ == "8":
            self.final_list.append("T")
            self.final_list.append("U")
            self.final_list.append("V")
            self.final_list.append("")
            
        elif digit_ == "9":
            self.final_list.append("W")
            self.final_list.append("X")
            self.final_list.append("Y")
            self.final_list.append("Z")
        
        elif digit_ == ("exit"):
            self.final_list.append('0')
            
        else:
            print("error in number conversion")
            
        # print self.final_list
        return self.final_list
        