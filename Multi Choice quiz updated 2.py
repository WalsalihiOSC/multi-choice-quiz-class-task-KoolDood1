# Multi Choice quiz (Andre)


from tkinter import *


class interface:
    def __init__(self, parent):
        self.input = StringVar()
        self.input.set("None")
        self.q = quizsystem() 
    
        question = Label(parent, text = self.q.question) #Question label
        question.pack(anchor= NW, pady = 5, padx = 5)

        for name in self.q.locations: #Loop to create radiobuttons
            radiobutton = Radiobutton(parent, variable = self.input, value = name, text = name, command= self.checkanswer)
            radiobutton.pack(anchor = N, pady = 5)
            
        self.result = Label(text = "") #Label that shows if you got it correct
        self.result.pack(anchor = N, pady = 10)

    def checkanswer(self): #Configures result label
        self.result.configure(text= self.q.displayanswer(self.input.get()))

        

class quizsystem: #Class with data encapsulation
    def __init__(self):
        self.question = "Question:           What is the capital of canada?"
        self.locations = ["Toronto", "Ottawa", "Montreal", "Ontario"]

        
    def displayanswer(self, answer):
        if answer == "Ottawa":
            return "Correct!"
        else:
            return "Incorrect!"
 


# Main routine
if __name__=="__main__":
    root = Tk()
    gui = interface(root)
    root.geometry("300x230")
    root.title("Multichoice quiz")
    root.mainloop()






