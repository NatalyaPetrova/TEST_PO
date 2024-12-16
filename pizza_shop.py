import tkinter as tk
from tkinter import messagebox
from pizza import Pizza
from order import Order
from customer import Customer


class PizzaShop:
    def __init__(self, master):
        self.master = master
        self.master.title("Pizza Shop")
        self.master.geometry("400x400")

        self.menu = [
            Pizza("Margherita", "Small", 7.99),
            Pizza("Margherita", "Medium", 9.99),
            Pizza("Margherita", "Large", 12.99),
            Pizza("Pepperoni", "Small", 8.99),
            Pizza("Pepperoni", "Medium", 10.99),
            Pizza("Pepperoni", "Large", 13.99),
            Pizza("Vegetarian", "Small", 7.49),
            Pizza("Vegetarian", "Medium", 9.49),
            Pizza("Vegetarian", "Large", 12.49)
        ]

        self.order = None
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.master, text="Welcome to the Pizza Shop!")
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(self.master, text="Enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(self.master, text="Enter your phone number:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.pack(pady=5)

        self.pizza_label = tk.Label(self.master, text="Select your pizzas:")
        self.pizza_label.pack()

        self.pizza_listbox = tk.Listbox(self.master)
        for pizza in self.menu:
            self.pizza_listbox.insert(tk.END, pizza.get_details())
        self.pizza_listbox.pack(pady=5)

        self.add_button = tk.Button(self.master, text="Add Pizza to Order", command=self.add_pizza)
        self.add_button.pack(pady=5)

        self.checkout_button = tk.Button(self.master, text="Checkout", command=self.checkout)
        self.checkout_button.pack(pady=10)

    def add_pizza(self):
        selected_pizza_index = self.pizza_listbox.curselection()
        if selected_pizza_index:
            selected_pizza = self.menu[selected_pizza_index[0]]
            if self.order is None:
                customer_name = self.name_entry.get()
                customer_phone = self.phone_entry.get()
                customer = Customer(customer_name, customer_phone)
                self.order = Order(customer.name)
            self.order.add_pizza(selected_pizza)
            messagebox.showinfo("Pizza Added", f"Added {selected_pizza.get_details()} to your order.")
        else:
            messagebox.showwarning("Selection Error", "Please select a pizza from the menu.")

    def checkout(self):
        if self.order:
            order_details = self.order.get_order_details()
            messagebox.showinfo("Order Summary", order_details)
        else:
            messagebox.showwarning("Order Error", "No pizzas in your order yet.")


def run_pizza_shop():
    root = tk.Tk()
    pizza_shop = PizzaShop(root)
    root.mainloop()


if __name__ == "__main__":
    run_pizza_shop()