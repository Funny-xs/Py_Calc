import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        N1 = float(entry1.get())
        N2 = float(entry2.get())
        op = operation_var.get()

        if op == '+':
            result = N1 + N2
        elif op == '-':
            result = N1 - N2
        elif op == '*':
            result = N1 * N2
        elif op == '/':
            result = N1 / N2
        else:
            messagebox.showerror("Error", "Please select an operation")
            return

        result_var.set(f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

# Create main window
root = tk.Tk()
root.title("Modern Typed Calculator")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Heading
tk.Label(root, text="Modern Typed Calculator", font=("Arial", 16, "bold"),
         bg="#2c3e50", fg="white").pack(pady=10)

# Entry frame
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=10)

tk.Label(frame, text="Number 1:", font=("Arial", 12), bg="#2c3e50", fg="white").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(frame, font=("Arial", 12))
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Number 2:", font=("Arial", 12), bg="#2c3e50", fg="white").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(frame, font=("Arial", 12))
entry2.grid(row=1, column=1, padx=5, pady=5)

# Operation selector
operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/']
tk.Label(root, text="Operation:", font=("Arial", 12), bg="#2c3e50", fg="white").pack(pady=5)
tk.OptionMenu(root, operation_var, *operations).pack(pady=5)

# Result display
result_var = tk.StringVar()
result_var.set("Result: ")
tk.Label(root, textvariable=result_var, font=("Arial", 14), bg="#2c3e50", fg="#1abc9c").pack(pady=10)

# Calculate button
tk.Button(root, text="Calculate", font=("Arial", 14), bg="#1abc9c", fg="white", width=12,
          command=calculate).pack(pady=10)

root.mainloop()
