class Inventory:
    def __init__(self, _capacity):
        self._capacity = _capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self._capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self._capacity

    def __repr__(self):
        items_for_print = ', '.join(self.items)
        return f"Items: {items_for_print}.\nCapacity left: {self._capacity - len(self.items)}"

