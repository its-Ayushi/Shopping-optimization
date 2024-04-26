import tkinter as tk
from tkinter import ttk

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

items = [
    Item("Apple", 0.5, 1),
    Item("Banana", 0.3, 0.5),
    Item("Orange", 0.4, 0.7),
    Item("Grapes", 0.6, 1.2),
    Item("Milk", 1.0, 1.5),
    Item("Bread", 0.8, 1.0),
    Item("Cheese", 0.7, 1.3),
    Item("Chicken", 1.2, 2.0),
    Item("Eggs", 0.2, 0.3),
    Item("Tomato", 0.3, 0.4),  # Additional items
    Item("Potato", 0.4, 0.6),
    Item("Carrot", 0.3, 0.5),
    Item("Spinach", 0.2, 0.3),
    Item("Onion", 0.3, 0.4),
    Item("Cucumber", 0.4, 0.5),
    Item("Watermelon", 1.5, 2.0),
    Item("Pineapple", 0.8, 1.2),
    Item("Strawberry", 0.2, 0.4),
]

weight_limit = 3.0  # Weight limit for carrying capacity

class ShoppingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Supermarket Shopping Optimization")
        self.geometry("800x600")  # Set the window size

        self.selected_items = []

        # Main frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)  # Fill the entire window

        # Canvas for displaying items
        self.canvas = tk.Canvas(self.main_frame, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame for controls
        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Label for available items
        self.items_label = tk.Label(self.control_frame, text="Available Items:", font=("Helvetica", 12))
        self.items_label.pack(padx=5, pady=5, anchor="w")

        # Combobox for selecting items
        self.items_dropdown = ttk.Combobox(self.control_frame, values=[item.name for item in items], state="readonly")
        self.items_dropdown.pack(padx=5, pady=5)

        # Button to add an item
        add_button = ttk.Button(self.control_frame, text="Add", command=self.add_item)
        add_button.pack(padx=5, pady=5)

        # Label for selected items
        self.selected_items_label = tk.Label(self.control_frame, text="Selected Items:", font=("Helvetica", 12))
        self.selected_items_label.pack(padx=5, pady=5, anchor="w")

        # Label for total weight
        self.total_weight_label = tk.Label(self.control_frame, text="", font=("Helvetica", 12))
        self.total_weight_label.pack(padx=5, pady=5, anchor="w")

        # Label for remaining weight capacity
        self.remaining_weight_label = tk.Label(self.control_frame, text="", font=("Helvetica", 12))
        self.remaining_weight_label.pack(padx=5, pady=5, anchor="w")

        # Button to remove an item
        remove_button = ttk.Button(self.control_frame, text="Remove", command=self.remove_item)
        remove_button.pack(padx=5, pady=5)

        # Button to optimize the shopping list
        optimize_button = ttk.Button(self.control_frame, text="Optimize", command=self.optimize_shopping_list)
        optimize_button.pack(padx=5, pady=5)

        # Draw knapsack table
        self.draw_knapsack_table()

    def add_item(self):
        item_name = self.items_dropdown.get()
        item = next((item for item in items if item.name == item_name), None)
        if item:
            self.selected_items.append(item)
            self.update_selected_items()

    def remove_item(self):
        if self.selected_items:
            self.selected_items.pop()
            self.update_selected_items()

    def update_selected_items(self):
        selected_items_text = "\n".join([item.name for item in self.selected_items])
        total_weight = sum([item.weight for item in self.selected_items])
        self.selected_items_label.config(text="Selected Items:\n" + selected_items_text)
        self.total_weight_label.config(text=f"Total Weight: {total_weight} kg")
        remaining_weight = max(weight_limit - total_weight, 0)
        self.remaining_weight_label.config(text=f"Remaining Weight Capacity: {remaining_weight} kg")

    def optimize_shopping_list(self):
        total_weight = sum([item.weight for item in self.selected_items])
        total_value = sum([item.value for item in self.selected_items])
        if total_weight > weight_limit:
            self.selected_items_label.config(text="Cannot optimize: Total weight exceeds limit")
        else:
            self.selected_items_label.config(text=f"Total Weight: {total_weight} kg\nTotal Value: {total_value}")

    def draw_knapsack_table(self):
        self.canvas.create_text(20, 20, text="Item", anchor="w")
        self.canvas.create_text(120, 20, text="Weight (kg)", anchor="w")
        self.canvas.create_text(220, 20, text="Value", anchor="w")

        y_offset = 40
        for item in items:
            self.canvas.create_text(20, y_offset, text=item.name, anchor="w")
            self.canvas.create_text(120, y_offset, text=item.weight, anchor="w")
            self.canvas.create_text(220, y_offset, text=item.value, anchor="w")
            y_offset += 20

if __name__ == "__main__":
    app = ShoppingApp()
    app.mainloop()
