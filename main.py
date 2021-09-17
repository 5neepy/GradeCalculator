from tkinter import *

root = Tk()
root.geometry("500x325")
root.title("Grade Calc")

# Text Labels
MaxBallText = Label(root, text="                    Max Points:                    ", font=("Calibri (Body)", 12))
YourBallText = Label(root, text="Your Points:", font=("Calibri (Body)", 12))

# Grid for text labels
MaxBallText.grid(row=0, column=0)
YourBallText.grid(row=0, column=1)

# Input
MaxBallInput = Entry(root, width=25,)
MaxBallInput.grid(row=1, column=0)

YourBallInput = Entry(root, width=25,)
YourBallInput.grid(row=1, column=1)

# Grade calc
def grade():
	sumgrade = format((int(YourBallInput.get())*6)/int(MaxBallInput.get()), '.2f')
	YourGrade = "Your grade is: " + str(sumgrade)
	LabelGrade = Label(root, text=YourGrade, font=("Consolas", 16))
	LabelGrade.grid(row=2, column=0)

# Submit Button
SubmitButton = Button(root, text="SUBMIT", padx=20, pady=5, command=grade)
SubmitButton.grid(row=3, column=1, pady=20)


# Custume Formula
DetailsForFormulaText = Label(root, text="Enter the details for custume formula:", font=("Calibri (Body)", 12))
DetailsForFormulaText.grid(row=4, column=0)

FormulaText = Label(root, text="x+(a/b)", font=("Calibri (Body)", 15))
FormulaText.grid(row=5, column=0)

# Text and pos for x, a, and b
x_text = Label(root, text="       x= ", font=("Consolas", 15))
x_text.grid(sticky="W", row=6, column=0)

a_text = Label(root, text="       a= ", font=("Consolas", 15))
a_text.grid(sticky="W", row=7, column=0)

b_text = Label(root, text="       b= ", font=("Consolas", 15))
b_text.grid(sticky="W", row=8, column=0)

# Input and pos for x, a, and b
x_input = Entry(root, width=5)
x_input.grid(row=6, column=0)

a_input = Entry(root, width=5)
a_input.grid(row=7, column=0)

b_input = Entry(root, width=5)
b_input.grid(row=8, column=0)

# Custum formula calc
def Custumformula():
	custumformulasum = format(int(x_input.get())+(int(a_input.get())/int(b_input.get())), '.2f')
	YourGrade = "Your grade is: " + str(custumformulasum)
	LabelGrade = Label(root, text=YourGrade, font=("Consolas", 12))
	LabelGrade.grid(row=7, column=1)

# Button 2
SubmitButton2 = Button(root, text="SUBMIT", padx=10, pady=3, command=Custumformula)
SubmitButton2.grid(row=8, column=1)


root.mainloop()
