# Multi Choice quiz (Andre)


from tkinter import *

class Mulitchoice:
    def __init__(self, parent):
        self.answer = StringVar()
        self.answer.set("None")

        self.question = Label(parent, text = "Question:           What is the capital of canada?")
        self.question.pack(anchor= NW, pady=5, padx=5)


        rb1 = Radiobutton(parent, variable = self.answer, value = "toronto", text = "Toronto", command = self.displayanswer)
        rb1.pack(anchor= N, pady=5)

        rb2 = Radiobutton(parent, variable = self.answer, value = "ottawa", text = "Ottawa", command = self.displayanswer)
        rb2.pack(anchor=N, pady= 5)
        
        rb3 = Radiobutton(parent, variable= self.answer, value = "montreal", text = "Montreal", command = self.displayanswer)
        rb3.pack(anchor= N, pady= 5)

        rb4 = Radiobutton(parent, variable= self.answer, value = "ontario", text = "Ontario", command = self.displayanswer)
        rb4.pack(anchor= N, pady=5)

        self.result = Label(text= "")
        self.result.pack(anchor= N, pady= 10)


    def displayanswer(self):
        answercheck = self.answer.get()
        if answercheck == "ottawa":
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



