# Multi Choice quiz (Andre)


from tkinter import *

class Mulitchoice:
    def __init__(self, parent):
        self.answer = StringVar()
        self.answer.set("None")

        self.question = Label(parent, text = "Question:           What is the capital of canada?")
        self.question.pack(anchor= NW, pady=5, padx=5)

        locations = ["Toronto", "Ottawa", "Montreal", "Ontario"]

        for item in locations:
            name = item
            radiobuttons = Radiobutton(parent, variable = self.answer, value = name, text = name, command = self.displayanswer )
            radiobuttons.pack(anchor = N, pady = 5)
            
        self.result = Label(text= "")
        self.result.pack(anchor= N, pady= 10)


    def displayanswer(self):
        answercheck = self.answer.get()
        if answercheck == "Ottawa":
            self.result.configure(text="Correct!")
        else:
            self.result.configure(text="Incorrect!") 
 


# Main routine
if __name__=="__main__":
    root = Tk()
    buttons = Mulitchoice (root)
    root.geometry("300x230")
    root.title("Multichoice quiz")
    root.mainloop()




