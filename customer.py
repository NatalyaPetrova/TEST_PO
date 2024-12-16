class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_details(self):
        return f"Customer: {self.name}, Phone: {self.phone}"

    def __str__(self):
        return self.get_details()
