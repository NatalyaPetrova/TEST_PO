class Pizza:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size  # Small, Medium, Large
        self.price = price

    def get_details(self):
        return f"{self.name} ({self.size}) - ${self.price:.2f}"

    def __str__(self):
        return self.get_details()
