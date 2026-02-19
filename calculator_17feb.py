import tkinter as tk
import math

memory = 0  # Global memory variable

def click(text):
    global memory
    if text == "=":
        try:
            result = eval(entry.get())
            result = round(result, 4)  # Round final result
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "Clear":
        entry.delete(0, tk.END)
    elif text == "⌫":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])    
    elif text == "M+":
        try:
            value = float(entry.get())
            memory += value
            entry.delete(0, tk.END)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "M-":
        try:
            value = float(entry.get())
            memory -= value
            entry.delete(0, tk.END)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "MR":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(memory))
    elif text == "MC":
        memory = 0
        entry.delete(0, tk.END)
    elif text == "sqrt":
        try:
            value = float(entry.get())
            if value < 0:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Error")
            else:
                result = round(math.sqrt(value), 4)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "x²":
        try:
            value = float(entry.get())
            result = round(value ** 2, 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "x³":
        try:
            value = float(entry.get())
            result = round(value ** 3, 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "1/x":
        try:
            value = float(entry.get())
            result = round(1 / value, 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "log":
        try:
            value = float(entry.get())
            result = round(math.log10(value), 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "sin":
        try:
            value = float(entry.get())
            result = round(math.sin(math.radians(value)), 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "cos":
        try:
            value = float(entry.get())
            result = round(math.cos(math.radians(value)), 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "tan":
        try:
            value = float(entry.get())
            result = round(math.tan(math.radians(value)), 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "pi":
        entry.insert(tk.END, str(round(math.pi, 4)))
    elif text == "∛":
        try:
            value = float(entry.get())
            if value < 0:
                result = -((-value) ** (1/3))
            else:
                result = value ** (1/3)
            result = round(result, 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "exp":
        try:
            value = float(entry.get())
            result = round(math.exp(value), 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "%":
        try:
            value = float(entry.get())
            result = round(value / 100, 4)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "^":
        entry.insert(tk.END,"**")        
    else:
        entry.insert(tk.END, text)

# --- Window ---
root = tk.Tk()
root.title("Scientific Calculator")

outer_frame = tk.Frame(root, bd=10, relief=tk.RIDGE, bg="black")
outer_frame.grid(row=0, column=0, sticky="nsew")

# --- Entry Box ---
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE,
                 justify="right", bg="Lightgray", fg="Black")
entry.grid(row=0, column=0, columnspan=6, sticky="nsew")

# --- Buttons Layout ---
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), ('sqrt', 1, 4), ('%', 1, 5),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('x²', 2, 4), ('1/x', 2, 5),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3), ('x³', 3, 4), ('log', 3, 5),
    ('0', 4, 0), ('Clear', 4, 1), ('=', 4, 2), ('/', 4, 3), ('sin', 4, 4), ('cos', 4, 5),
    ('tan', 5, 0), ('pi', 5, 1), ('exp', 5, 2), ('(', 5, 3), (')', 5, 4), ('^', 5, 5),
    ('M+', 6, 0), ('M-', 6, 1), ('MR', 6, 2), ('MC', 6, 3), ('⌫', 6, 4), ('∛', 6, 5)
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, font=("Arial", 16),
                    bg="black", fg="White",
                    command=lambda t=text: click(t))
    btn.grid(row=row, column=col, sticky="nsew")

# --- Grid Weight ---
for i in range(7):   # rows
    root.grid_rowconfigure(i, weight=1)
for j in range(6):   # columns
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
