import tkinter as tk

root = tk.Tk()

root.title("Basic Form")
root.geometry("500x600")

def submit_form():
    value = entry.get()
    output_label.config(text=value) #config  le text ko value modify grxa
    print(value)

label = tk.Label(root, text="Your Name")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=submit_form)
button.pack()

output_label = tk.Label(root, text="") 
output_label.pack() 

root.mainloop()