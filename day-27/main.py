from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)


result = 0


def calculate():
    convert = float(input_miles.get()) * 1.60934
    my_label.config(text=round(convert, 2))

    input_miles.delete(0, END)


input_miles = Entry(width=15)
input_miles.grid(column=2, row=1)

text1 = Label(text=f"Miles", font=("Arial", 24))
text1.grid(column=3, row=1)

text2 = Label(text=f"is equal to ", font=("Arial", 24))
text2.grid(column=1, row=2)

my_label = Label(text=f"{result}", font=("Arial", 24))
my_label.grid(column=2, row=2)

text3 = Label(text=f"Km", font=("Arial", 24))
text3.grid(column=3, row=2)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=2, row=3)


window.mainloop()
