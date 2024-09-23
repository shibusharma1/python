import tkinter as tk

root = tk.Tk()

root.title("Basic Form")
root.geometry("500x600")

def submit_form():
    value = entry.get()
    output_label.config(text=value)
    print(value)

label = tk.Label(root, text="Your Name")
label.grid(row=0, column=0)  # Grid label in row 0, column 0

entry = tk.Entry(root)
entry.grid(row=0, column=1)  # Grid entry in row 0, column 1

button = tk.Button(root, text="Submit", command=submit_form)
button.grid(row=1, column=0, columnspan=2)  # Grid button in row 1, spanning both columns

output_label = tk.Label(root, text="")
output_label.grid(row=2, column=0, columnspan=2)  # Grid output label in row 2, spanning both columns

root.mainloop()