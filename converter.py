from tkinter import *



window = Tk()
window.minsize(width=500, height=300)
window.title("Mile to Km Converter")


def button_clicked():
    
    input_value = float(input.get())
    km = input_value * 1.6
    out_put.config(text=f"{km}")


input = Entry()
input.grid(row=0, column=1)



miles_label = Label(text="Miles").grid(row=0, column=2)


equal_label = Label(text="Equale to")
equal_label.grid(row=1, column=0)

out_put = Label(text="0")
out_put.grid(row=1, column=1)

kilos_label = Label(text="KM")
kilos_label.grid(row=1, column=2)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(row=2, column=1)





window.mainloop()