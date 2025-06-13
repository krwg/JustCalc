

#     ____.               __   _________        .__          
#    |    |__ __  _______/  |_ \_   ___ \_____  |  |   ____  
#    |    |  |  \/  ___/\   __\/    \  \/\__  \ |  | _/ ___\ 
#/\__|    |  |  /\___ \  |  |  \     \____/ __ \|  |_\  \___ 
#\________|____//____  > |__|   \______  (____  /____/\___  >
#                    \/                \/     \/          \/ 



import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

#krwg


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry_text = f"{result:.{decimal_precision}f}"
        entry.insert(0, entry_text)
        #krwg
        if history_enabled:
            history_text.insert(tk.END, f"{entry.get()} = {entry_text}\n")
            history_text.see(tk.END)
    except (SyntaxError, NameError, ZeroDivisionError):
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def handle_button_press(text):
    if text == '=':
        button_equal()
    elif text == 'C':
        button_clear()
    elif text == '<':
        button_delete()
    else:
        button_click(text)

def change_theme(theme):
    global current_theme
    current_theme = theme
    update_theme()

def update_theme():
    if current_theme == "light":
        window.configure(bg="#F5F5F5")  
        entry.configure(bg="#F5F5F5", fg="#212121", font=("Roboto", 30), insertbackground="#212121")  
        for button in buttons_list:
            button.configure(bg="#EEEEEE", fg="#212121", relief="flat", borderwidth=0, font=("Roboto", 22))  
        button_clear.configure(bg="#EEEEEE", fg="#D32F2F", relief="flat", borderwidth=0, font=("Roboto", 22))  
        delete_button.configure(bg="#EEEEEE", fg="#757575", relief="flat", borderwidth=0, font=("Roboto", 22))  
        settings_button.configure(bg="#EEEEEE", fg="#757575", relief="flat", borderwidth=0, font=("Roboto", 18))  
        history_button.configure(bg="#EEEEEE", fg="#757575", relief="flat", borderwidth=0, font=("Roboto", 18))  
        settings_frame.configure(bg="#F5F5F5")
        history_frame.configure(bg="#F5F5F5")
        for widget in settings_frame.winfo_children():
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
                widget.configure(bg="#F5F5F5", fg="#212121")
        
        history_text.configure(bg="#FAFAFA", fg="#212121") 
        for button in precision_buttons:
            button.configure(bg="#EEEEEE", fg="#212121", relief="flat", borderwidth=0, font=("Roboto", 16), padx=8)

    elif current_theme == "dark":
        window.configure(bg="#212121") 
        entry.configure(bg="#212121", fg="#FAFAFA", font=("Roboto", 30), insertbackground="#FAFAFA")  
        for button in buttons_list:
            button.configure(bg="#424242", fg="#FAFAFA", relief="flat", borderwidth=0, font=("Roboto", 22))  
        button_clear.configure(bg="#424242", fg="#EF5350", relief="flat", borderwidth=0, font=("Roboto", 22))  
        delete_button.configure(bg="#424242", fg="#BDBDBD", relief="flat", borderwidth=0, font=("Roboto", 22))  
        settings_button.configure(bg="#424242", fg="#BDBDBD", relief="flat", borderwidth=0, font=("Roboto", 18)) 
        history_button.configure(bg="#424242", fg="#BDBDBD", relief="flat", borderwidth=0, font=("Roboto", 18))  
        settings_frame.configure(bg="#212121")
        history_frame.configure(bg="#212121")
        for widget in settings_frame.winfo_children():
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
                widget.configure(bg="#212121", fg="#FAFAFA")  
       
        history_text.configure(bg="#303030", fg="#FAFAFA")  
        for button in precision_buttons:
            button.configure(bg="#424242", fg="#FAFAFA", relief="flat", borderwidth=0, font=("Roboto", 16), padx=8)

    elif current_theme == "moon":
        window.configure(bg="#000000")  
        entry.configure(bg="#000000", fg="#EEEEEE", font=("Roboto", 30), insertbackground="#EEEEEE")  
        for button in buttons_list:
            button.configure(bg="#212121", fg="#EEEEEE", relief="flat", borderwidth=0, font=("Roboto", 22))  
        button_clear.configure(bg="#212121", fg="#F44336", relief="flat", borderwidth=0, font=("Roboto", 22))  
        delete_button.configure(bg="#212121", fg="#9E9E9E", relief="flat", borderwidth=0, font=("Roboto", 22))  
        settings_button.configure(bg="#212121", fg="#9E9E9E", relief="flat", borderwidth=0, font=("Roboto", 18))  
        history_button.configure(bg="#212121", fg="#9E9E9E", relief="flat", borderwidth=0, font=("Roboto", 18))  
        settings_frame.configure(bg="#000000")
        history_frame.configure(bg="#000000")
        for widget in settings_frame.winfo_children():
            if isinstance(widget, tk.Button) or isinstance(widget, tk.Label):
                widget.configure(bg="#000000", fg="#EEEEEE")  
        
        history_text.configure(bg="#121212", fg="#EEEEEE") 
        for button in precision_buttons:
            button.configure(bg="#212121", fg="#EEEEEE", relief="flat", borderwidth=0, font=("Roboto", 16), padx=8)

def about_window():
    about_text = """
    JustCalc
    Moonstone 1.2

    Developer: krwg
    Year: 2025

    Description:
    JustCalc is a modern and convenient calculator, 
    designed to perform basic arithmetic operations.

    Features:
    - Addition, subtraction, multiplication, division
    - Floating-point number support
    - Calculation history
    - Precision settings

    Libraries used:
    - Tkinter

    Acknowledgements:
    - Icons: Flaticon

    Contact Information:
    - GitHub - https://github.com/krwg

    """


    about_window = tk.Toplevel(window)
    about_window.title("About JustCalc")

   
    about_window.geometry("400x500")  

    
    label = tk.Label(about_window, text=about_text, justify=tk.LEFT, font=("Arial", 12)) 
    label.pack(padx=10, pady=10, fill="both", expand=True) 
def toggle_settings_menu():
    if settings_frame.winfo_ismapped():
        settings_frame.grid_forget()
    else:
        settings_frame.grid(row=row_num + 1, column=start_col + 1, padx=5, pady=5, sticky="nw")

def toggle_history():
    if history_frame.winfo_ismapped():
        history_frame.grid_forget()
    else:
        history_frame.grid(row=row_num + 1, column=start_col + 2, padx=5, pady=5, sticky="nw")

def toggle_history_enabled():
    global history_enabled
    history_enabled = not history_enabled
    if history_enabled:
        history_enabled_button.config(text="Disable History")
    else:
        history_enabled_button.config(text="Enable History")

def set_decimal_precision(precision):
    global decimal_precision
    decimal_precision = precision

def close_window():
    window.destroy()

current_theme = "light"
decimal_precision = 2
history_enabled = True

window = tk.Tk()
window.title("JustCalc")


window.grid_rowconfigure(0, weight=2)  
for i in range(1, 10):
    window.grid_rowconfigure(i, weight=1)
for i in range(8):
    window.grid_columnconfigure(i, weight=1)




entry = tk.Entry(window, width=25, borderwidth=0, relief="flat", font=("Roboto", 30), justify='right') 
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


buttons_list = []
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '<'
]

start_row = 1
start_col = 0
row_num = start_row
col_num = start_col
for button_text in buttons:
    if button_text == '<':
        delete_button = tk.Button(window, text=button_text, padx=20, pady=10, command=lambda: handle_button_press(button_text),
                           font=("Roboto", 22), relief="flat", bd=0) 
        delete_button.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")
        buttons_list.append(delete_button)
    else:
        button = tk.Button(window, text=button_text, padx=20, pady=10,
                           command=lambda text=button_text: handle_button_press(text),
                           font=("Roboto", 22), relief="flat", bd=0) 
        button.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")
        buttons_list.append(button)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1


button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear,
                         font=("Roboto", 22), relief="flat", bd=0) 
button_clear.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")
buttons_list.append(button_clear)


settings_button = tk.Button(window, text="Settings", padx=20, pady=10, command=toggle_settings_menu,
                           font=("Roboto", 18), relief="flat", bd=0)
settings_button.grid(row=row_num, column=col_num + 1, padx=5, pady=5, sticky="nsew")


history_button = tk.Button(window, text="History", padx=20, pady=10, command=toggle_history,
                          font=("Roboto", 18), relief="flat", bd=0)  
history_button.grid(row=row_num, column=col_num + 2, padx=5, pady=5, sticky="nsew")

#krwg
settings_frame = tk.Frame(window)


light_theme_button = tk.Button(settings_frame, text="Light", padx=10, pady=5, command=lambda: change_theme("light"), relief="flat", bd=0, font=("Roboto", 18))  
light_theme_button.grid(row=0, column=0, padx=2, pady=2, sticky="ew")

dark_theme_button = tk.Button(settings_frame, text="Dark", padx=10, pady=5, command=lambda: change_theme("dark"), relief="flat", bd=0, font=("Roboto", 18))  
dark_theme_button.grid(row=1, column=0, padx=2, pady=2, sticky="ew")

moon_theme_button = tk.Button(settings_frame, text="Moon", padx=10, pady=5, command=lambda: change_theme("moon"), relief="flat", bd=0, font=("Roboto", 18))  
moon_theme_button.grid(row=2, column=0, padx=2, pady=2, sticky="ew")


about_button = tk.Button(settings_frame, text="About", padx=10, pady=5, command=about_window, relief="flat", bd=0, font=("Roboto", 18)) 
about_button.grid(row=3, column=0, padx=2, pady=2, sticky="ew")


exit_button = tk.Button(settings_frame, text="Exit", padx=10, pady=5, command=close_window, relief="flat", bd=0, font=("Roboto", 18)) 
exit_button.grid(row=4, column=0, padx=2, pady=2, sticky="ew")


history_enabled_button = tk.Button(settings_frame, text="Disable History", padx=10, pady=5, command=toggle_history_enabled, relief="flat", bd=0, font=("Roboto", 18)) 
history_enabled_button.grid(row=6, column=0, padx=2, pady=2, sticky="ew")


precision_frame_label = tk.Label(settings_frame, text="Decimal Precision:") 
precision_frame_label.grid(row=5, column=0, padx=2, pady=2, sticky="ew")


precision_buttons = []
precision_2_button = tk.Button(settings_frame, text="2", padx=8, pady=2, command=lambda: set_decimal_precision(2), relief="flat", bd=0, font=("Roboto", 16))  
precision_2_button.grid(row=5, column=1, padx=2, pady=2, sticky="ew")
precision_buttons.append(precision_2_button)
precision_4_button = tk.Button(settings_frame, text="4", padx=8, pady=2, command=lambda: set_decimal_precision(4), relief="flat", bd=0, font=("Roboto", 16))  
precision_4_button.grid(row=5, column=2, padx=2, pady=2, sticky="ew")
precision_buttons.append(precision_4_button)
precision_8_button = tk.Button(settings_frame, text="8", padx=8, pady=2, command=lambda: set_decimal_precision(8), relief="flat", bd=0, font=("Roboto", 16))  
precision_8_button.grid(row=5, column=3, padx=2, pady=2, sticky="ew")
precision_buttons.append(precision_8_button)


for i in range(7):
    settings_frame.grid_rowconfigure(i, weight=1)
settings_frame.grid_columnconfigure(0, weight=1)


history_frame = tk.Frame(window)
history_text = scrolledtext.ScrolledText(history_frame, width=30, height=10, font=("Arial", 12))
history_text.pack(expand=True, fill="both")

update_theme()
#krwg
window.mainloop()