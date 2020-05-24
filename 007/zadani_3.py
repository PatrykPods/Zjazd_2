import tkinter
from tkinter import messagebox
def oblicz():
    try:
        val_a = float(a_entry.get())
        val_b = float(b_entry.get())
        val_c = float(c_entry.get())
        koszt = ((val_c / 100) * val_b) * val_a
        wynik.configure(text=koszt)
    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")
root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="koszt paliwa")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="spalanie samochodu")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

c_label = tkinter.Label(master=root, text="dystans")
c_label.pack()
c_entry = tkinter.Entry(master=root)
c_entry.pack()

wynik_labl = tkinter.Label(master=root, text="Wynik:")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()

submit = tkinter.Button(master=root, text="Policz", command=oblicz)
submit.pack()

root.mainloop()