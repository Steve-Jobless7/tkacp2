import tkinter as tk

def convert():
    temp = entry.get()
    if temp:
        temp = float(temp)
        if var.get() == "C to F":
            result = (temp * 9/5) + 32
            label_result.config(text=f"{result:.2f} °F")
        else:
            result = (temp - 32) * 5/9
            label_result.config(text=f"{result:.2f} °C")

root = tk.Tk()
root.title("Temperature Converter")

entry = tk.Entry(root)
entry.pack(pady=10)

var = tk.StringVar(value="C to F")
tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value="C to F").pack()
tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value="F to C").pack()

tk.Button(root, text="Convert", command=convert).pack(pady=10)
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()