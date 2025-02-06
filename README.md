# Shopping Optimization using Knapsack

## Overview

The **Supermarket Shopping Optimization App** is a Python-based GUI application built using the Tkinter library. It helps users manage their shopping list by allowing them to select items based on weight and value, with an optimized approach to stay within a specified weight limit. Users can add or remove items, view the total weight and value of the shopping list, and optimize it to maximize the total value while ensuring it does not exceed the weight limit.

### Features:
- **Dynamic Item Selection**: Add or remove items to/from the shopping list.
- **Weight and Value Calculation**: Displays total weight and value of selected items.
- **Remaining Weight Capacity**: Indicates how much more weight can be added to the cart.
- **Optimization**: Allows the user to see the total weight and value and check if the shopping list is optimized.
- **Knapsack Table**: Visual representation of available items with their weight and value.

## Installation

To run the **Supermarket Shopping Optimization App**, follow these steps:

### Step 1: Clone or Download the Repository
First, clone or download this repository to your local machine.

```bash
git clone https://github.com/yourusername/supermarket-shopping-optimization.git
```

Alternatively, you can download the ZIP file from the repository's GitHub page and extract it to a folder on your machine.

### Step 2: Install Python 3.x

This application requires **Python 3.x**. You can download Python from the official website:

- [Download Python](https://www.python.org/downloads/)

After installing Python, ensure it’s added to your system's PATH.

### Step 3: Install Tkinter (if not installed)

Tkinter is typically pre-installed with Python. However, if it’s not installed on your system, you can install it by running the following command:

#### For Ubuntu/Debian-based Linux systems:
```bash
sudo apt-get install python3-tk
```

#### For macOS, Tkinter should come with Python by default. If it’s missing, install it via Homebrew:
```bash
brew install python-tk
```

#### For Windows:
Tkinter is generally bundled with Python. If missing, reinstall Python and select the option to install Tkinter during installation.

### Step 4: Run the Application

Once the dependencies are installed, navigate to the project folder and run the Python script:

```bash
python app.py
```

This will launch the application, opening the graphical interface for interacting with the shopping optimization tool.

## Application Interface

- **Dropdown Menu**: A combobox to select items from a predefined list of available supermarket items.
- **Add and Remove Buttons**: To dynamically add and remove items from the shopping list.
- **Optimization Button**: Calculates the total weight and value of the selected items and checks if it exceeds the weight limit.
- **Knapsack Table**: Displays a list of available items along with their weights and values for reference.

## Example of Using the Application

1. **Select Items**: From the dropdown, select items (e.g., Apple, Banana, etc.).
2. **Add Item**: Click the "Add" button to add the selected item to your shopping list.
3. **Remove Item**: If you want to remove an item, click the "Remove" button (removes the most recently added item).
4. **View Calculations**: The app will automatically calculate the total weight and value, as well as the remaining weight capacity.
5. **Optimize**: Click the "Optimize" button to check if the shopping list is within the weight limit and see the optimized total weight and value.

## Conclusion

This simple tool can be a great way to efficiently manage your shopping list, ensuring that you don’t exceed a specific weight limit while also considering the value of the items you’re adding. You can expand this application by adding more features, like prioritizing items based on specific criteria or adjusting the weight limit dynamically.

Enjoy using the Supermarket Shopping Optimization App!
