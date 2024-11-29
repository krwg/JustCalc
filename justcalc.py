import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except (SyntaxError, NameError, ZeroDivisionError):
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def change_theme(theme):
    global current_theme
    current_theme = theme
    update_theme()

def update_theme():
    if current_theme == "light":
        window.configure(bg="#f0f0f0")
        entry.configure(bg="white", fg="black")
        for button in buttons_list:
            button.configure(bg="#2196F3", fg="white") 
    else:
        window.configure(bg="#333")
        entry.configure(bg="#444", fg="white")
        for button in buttons_list:
            button.configure(bg="#555", fg="white")


current_theme = "light"

window = tk.Tk()
window.title("JustCalc")


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Светлая тема", command=lambda: change_theme("light"))
filemenu.add_command(label="Темная тема", command=lambda: change_theme("dark"))
filemenu.add_separator()
filemenu.add_command(label="Выход", command=window.quit)
menubar.add_cascade(label="Настройки", menu=filemenu)
window.config(menu=menubar)



entry = tk.Entry(window, width=25, borderwidth=5, relief="groove", font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons_list = []


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(window, text=button_text, padx=20, pady=10,
                       command=lambda text=button_text: button_click(text) if text != '=' else button_equal() if text == '=' else button_clear() if text == 'C' else None,
                       font=("Arial", 16), bg="#2196F3", fg="white", relief="raised", bd=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    buttons_list.append(button)
    col += 1
    if col > 3:
        col = 0
        row += 1


button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear,
                         font=("Arial", 16), bg="#FF5722", fg="white", relief="raised", bd=2)
button_clear.grid(row=row, column=col, padx=5, pady=5)
buttons_list.append(button_clear)


update_theme()

window.mainloop()