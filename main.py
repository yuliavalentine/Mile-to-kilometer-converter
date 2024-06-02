from tkinter import *

# create screen
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# create all labels
miles_label = Label(text="Miles", font=("Arial", 14, "italic"))
miles_label.grid(row=0, column=2)

km_label = Label(text="Km", font=("Arial", 14, "italic"))
km_label.grid(row=1, column=2)

is_equal_to_label = Label(text="is equal to", font=("Arial", 14, "italic"))
is_equal_to_label.grid(row=1, column=0)

result_text = 0
result_label = Label(text=result_text, font=("Arial", 14, "italic"))

result_label.grid(row=1, column=1)


# create button

def button_miles_to_km():
    result_label.config(text=round(float(input.get()) * 1.609344, 1))


button = Button(text="Calculate", command=button_miles_to_km)
button.grid(row=2, column=1)

# create input box

input = Entry()
input.get()
input.grid(row=0, column=1)

window.mainloop()
