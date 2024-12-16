class Order:
    def __init__(self, customer_name, pizzas=None):
        if pizzas is None:
            pizzas = []
        self.customer_name = customer_name
        self.pizzas = pizzas

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        return sum(pizza.price for pizza in self.pizzas)

    def get_order_details(self):
        details = [f"Order for {self.customer_name}:"]
        for pizza in self.pizzas:
            details.append(f"  - {pizza.get_details()}")
        details.append(f"Total: ${self.calculate_total():.2f}")
        return "\n".join(details)

    def __str__(self):
        return self.get_order_details()