import tkinter as tk

root = tk.Tk()

root.title("Registration Form")
root.geometry("500x500")  # Set window size to 200x200

def submit_form():
    value = entry.get()
    output_label.config(text=value)
    print(value)


frame = tk.Frame(root, bg="white")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  


heading_label = tk.Label(frame, text="Registration Form", font=("Arial", 20, "bold"))
heading_label.pack(pady=10)  

label = tk.Label(frame, text="Your Name")
label.pack()

entry = tk.Entry(frame)
entry.pack()

button = tk.Button(frame, text="Submit", command=submit_form)
button.pack(pady=10)  # Add some padding around the button

output_label = tk.Label(frame, text="")
output_label.pack()

root.mainloop()