import tkinter as tk

root = tk.Tk()
root.geometry("500x1000")

# 1. Label Widget

# A label widget is used to display text or images on the screen. 
# You can create a label widget using the Label class:

label = tk.Label(root, text="Hello, World!")
label.pack()

# You can customize the label widget by using various options, such as:

# text: sets the text to be displayed
# font: sets the font of the text
# fg: sets the foreground color of the text
# bg: sets the background color of the label


# 2. Button Widget

# A button widget is used to create a clickable button on the screen. 
# You can create a button widget using the Button class:

button = tk.Button(root, text="Click Me!")
button.pack()

# You can customize the button widget by using various options, such as:

# text: sets the text to be displayed on the button
# command: sets the function to be called when the button is clicked
# fg: sets the foreground color of the button
# bg: sets the background color of the button

# 3. Entry Widget

# An entry widget is used to create a text entry field on the screen. 
# You can create an entry widget using the Entry class:

entry = tk.Entry(root)
entry.pack()




# You can customize the entry widget by using various options, such as:

# width: sets the width of the entry field
# font: sets the font of the text
# fg: sets the foreground color of the text
# bg: sets the background color of the entry field

# 4. Text Widget

# A text widget is used to create a multi-line text entry field on the screen. 
# You can create a text widget using the Text class:

text = tk.Text(root)
text.pack()

# 5. Checkbutton Widget

# A checkbutton widget is used to create a checkbox on the screen. 
# You can create a checkbutton widget using the Checkbutton class:

checkbutton = tk.Checkbutton(root, text="Check Me!")
checkbutton.pack()

# You can customize the checkbutton widget by using various options, such as:

# text: sets the text to be displayed next to the checkbox
# variable: sets the variable to be associated with the checkbox
# onvalue: sets the value to be assigned to the variable when the checkbox is checked
# offvalue: sets the value to be assigned to the variable when the checkbox is unchecked

# 6. Radiobutton Widget

# A radiobutton widget is used to create a radio button on the screen. 
# You can create a radiobutton widget using the Radiobutton class:

radiobutton = tk.Radiobutton(root, text="Select Me!")
radiobutton.pack()

# You can customize the radiobutton widget by using various options, such as:

# text: sets the text to be displayed next to the radio button
# variable: sets the variable to be associated with the radio button
# value: sets the value to be assigned to the variable when the radio button is selected


# The Listbox widget in Tkinter is a multi-item widget that displays a list of items from which 
# the user can select one or more items. 
# Here's a more detailed look at the Listbox widget:

listbox = tk.Listbox(root)
listbox.pack()

listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")



root.mainloop()