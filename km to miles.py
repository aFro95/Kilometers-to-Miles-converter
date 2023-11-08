from tkinter import *

def kilometers_to_miles():
    kilometers = float(kilometer_input.get())
    miles = round(kilometers * 0.621371192, 2)
    miles_result_label.config(text=f"{miles}")


window = Tk()
window.title("Kilometer to Miles Converter")
window.config(padx=20, pady=20)

kilometer_input = Entry(width=7)
kilometer_input.grid(column=1, row=0)

kilometer_label = Label(text="Kilometer")
kilometer_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_result_label = Label(text="0")
miles_result_label.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=kilometers_to_miles)
calculate_button.grid(column=1, row=2)

window.mainloop()