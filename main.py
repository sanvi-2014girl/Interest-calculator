import tkinter as tk
from tkinter import messagebox
def calculate_simple_interest(principal,rate,time):
    return(principal * rate* time) / 100
def calculate_compound_interest(principal,rate,time):
    return principal * ((1 + rate / 100)** time-1)
def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        simple_interest = calculate_simple_interest(principal , rate , time)
        compound_interest = calculate_compound_interest(principal , rate , time)
        messagebox.showinfo("Result",
                            f"Simple Interest:{simple_interest:.2f}\nCompound Interest:{compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("Error","Please enter valid numerical values")
root = tk.Tk()
root.title("Interest Calculator")
tk.Label(root,text="principal amount: ").grid(row=0,coloumn=0,padx=10,pady=10)
entry_principal = tk.Entry(root)
entry_principal.grid(row=0,column=1,padx=10,pady=10)
tk.Label(root, text="Rate of Interest (%):").grid(row=1,column=0,padx=10,pady=10)
entry_rate = tk.Entry(root)
entry_rate.grid(row=1,coloumn=1,padx=10,pady=10)
tk.Label(root, text="Time Period(years):").grid(row=2,column=0,padx=10,pady=10)
entry_time = tk.Entry(root)
entry_time.grid(row=2,column=1,padx=10,pady=10)
btn_calculate = tk.Button(root, text="Calculate Interest", command=calculate_interest)
btn_calculate.grid(row=3,columnspan=2,padx=10,pady=10)
root.mainloop()