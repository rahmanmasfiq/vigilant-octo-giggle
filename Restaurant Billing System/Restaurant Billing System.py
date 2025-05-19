# Refactored Restaurant Billing System with OOP, Exception Handling, Discounts, and Save Feature
import tkinter as tk
from tkinter import messagebox, filedialog
import random
import time

# =================== OOP Classes ======================
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, menu_item, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.menu_item = menu_item
        self.quantity = quantity

    def get_cost(self):
        return self.menu_item.price * self.quantity


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        self.items.append(OrderItem(menu_item, quantity))

    def get_subtotal(self):
        return sum(item.get_cost() for item in self.items)


class Bill:
    def __init__(self, order, vat_percent=0, discount_percent=0):
        self.order = order
        self.vat_percent = vat_percent
        self.discount_percent = discount_percent

    def calculate_total(self):
        subtotal = self.order.get_subtotal()
        discount = (subtotal * self.discount_percent) / 100
        subtotal_after_discount = subtotal - discount
        vat = (subtotal_after_discount * self.vat_percent) / 100
        return subtotal_after_discount + vat

    def generate_bill_text(self, ref_no):
        lines = [f"Reference No: {ref_no}"]
        lines.append(f"Date: {time.strftime('%d/%m/%Y')}")
        lines.append("-" * 40)
        for item in self.order.items:
            lines.append(f"{item.menu_item.name} x {item.quantity} = {item.get_cost()} Tk")
        lines.append("-" * 40)
        lines.append(f"Subtotal: {self.order.get_subtotal()} Tk")
        lines.append(f"Discount: {self.discount_percent}%")
        lines.append(f"VAT: {self.vat_percent}%")
        lines.append(f"Total: {self.calculate_total()} Tk")
        return "\n".join(lines)

    def save_bill(self, ref_no):
        bill_text = self.generate_bill_text(ref_no)
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt",
                                         filetypes=[("Text Files", "*.txt")])
        if file:
            file.write(bill_text)
            file.close()


# ==================== GUI Layer =====================
class BillingSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x700")
        self.root.title("Restaurant Billing System (OOP)")
        self.root.configure(bg='#f0f0f0')

        # Menu Items
        self.menu = {
            "Chicken Burger": MenuItem("Chicken Burger", 160),
            "Beef Burger": MenuItem("Beef Burger", 180),
            "French Fries": MenuItem("French Fries", 80),
            "Soft Drink": MenuItem("Soft Drink", 20)
        }

        # GUI Variables
        self.quantities = {item: tk.StringVar(value="0") for item in self.menu}
        self.vat = tk.StringVar(value="0")
        self.discount = tk.StringVar(value="0")
        self.bill_text = tk.StringVar(value="")


        self.build_gui()

    def build_gui(self):
        title_label = tk.Label(self.root, text="Smak Restaurant ", font=("Arial", 24, "bold"), bg="#2bbe37", fg='#333')
        title_label.pack(pady=20)

        frame = tk.Frame(self.root, bg='#ffffff', bd=2, relief="ridge")
        frame.pack(padx=20, pady=20, fill='both', expand=True)

        input_frame = tk.Frame(frame, bg='#ffffff')
        input_frame.pack(side='left', padx=20, pady=20, anchor='n')

        display_frame = tk.Frame(frame, bg='#ffffff')
        display_frame.pack(side='right', padx=20, pady=20, anchor='n')

        row = 0
        for name in self.menu:
            tk.Label(input_frame, text=f"{name} ({self.menu[name].price} Tk)", font=("Arial", 14), bg='#ffffff').grid(row=row, column=0, padx=10, pady=5, sticky='w')
            tk.Entry(input_frame, textvariable=self.quantities[name], font=("Arial", 14), width=10).grid(row=row, column=1)
            row += 1

        tk.Label(input_frame, text="VAT (%)", font=("Arial", 14), bg='#ffffff').grid(row=row, column=0, padx=10, pady=5, sticky='w')
        tk.Entry(input_frame, textvariable=self.vat, font=("Arial", 14), width=10).grid(row=row, column=1)
        row += 1

        tk.Label(input_frame, text="Discount (%)", font=("Arial", 14), bg='#ffffff').grid(row=row, column=0, padx=10, pady=5, sticky='w')
        tk.Entry(input_frame, textvariable=self.discount, font=("Arial", 14), width=10).grid(row=row, column=1)
        row += 1

        tk.Button(input_frame, text="Generate Bill", command=self.generate_bill, font=("Arial", 14), bg='#4CAF50', fg='white', width=15).grid(row=row, column=0, pady=20)
        tk.Button(input_frame, text="Save Bill", command=self.save_bill, font=("Arial", 14), bg='#2196F3', fg='white', width=15).grid(row=row, column=1, pady=20)

        self.bill_area = tk.Label(display_frame, textvariable=self.bill_text, font=("Courier", 12), justify='left', anchor='nw', bg='#f9f9f9', bd=2, relief="sunken", width=50, height=30, padx=10, pady=10)
        self.bill_area.pack()

    def generate_bill(self):
        try:
            order = Order()
            for name, var in self.quantities.items():
                qty = int(var.get())
                if qty < 0:
                    raise ValueError(f"Quantity for {name} cannot be negative.")
                if qty > 0:
                    order.add_item(self.menu[name], qty)

            vat_percent = float(self.vat.get())
            discount_percent = float(self.discount.get())

            bill = Bill(order, vat_percent, discount_percent)
            ref_no = f"BILL{random.randint(1000, 9999)}"
            self.bill_text.set(bill.generate_bill_text(ref_no))

        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def save_bill(self):
        try:
            if not self.bill_text.get():
                messagebox.showwarning("Warning", "No bill to save.")
                return
            ref_no = f"BILL{random.randint(1000, 9999)}"
            bill_text = self.bill_text.get()
            file = filedialog.asksaveasfile(mode='w', defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
            if file:
                file.write(bill_text)
                file.close()
                messagebox.showinfo("Saved", "Bill saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save bill: {e}")


# Running the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = BillingSystemGUI(root)
    root.mainloop()

