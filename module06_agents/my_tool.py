# my_tool.py
# Author: Lexy Lichtenstein


class MenuLookup:
    """A tool that knows the menu and hours. It knows nothing about chatting."""

    # Saves the menu and hours on this object so the other methods can use them
    # and starts an empty list for pickup orders the manager has approved
    def __init__(self, menu, hours):
        """Store the menu (item to price) and the opening hours."""
        self.menu = menu
        self.hours = hours
        self.orders = []

    # Loops through every menu item and returns the first one found in the customer's message
    # I use .lower() so capital letters don't matter, and None means nothing matched
    def find_item(self, text):
        """Return the first menu item mentioned in text, or None."""
        for item in self.menu:
            if item in text.lower():
                return item
        return None

    # Looks up one item's price in the menu, or returns None if it isn't on the menu
    def price_for(self, item):
        """Return the price of one item, or None if it is not on the menu."""
        if item in self.menu:
            return self.menu[item]
        return None

    # Gives back the opening hours that were saved when the tool was created
    def get_hours(self):
        """Return the opening hours."""
        return self.hours

    # The tool the model may ask for. A program reads this docstring, so the Args section matters
    def look_up_price(self, item):
        """Look up the price of one menu item.

        Args:
            item: The menu item, like burger.
        """
        # Finds the menu item in the text, or None if there is no match
        found = self.find_item(item)
        # Tells the model the item is not on the menu so it can ask the customer
        if found is None:
            return "That item is not on the menu. Try an item like burger."
        # Builds the answer from the menu data, not from the model's memory
        return f"The {found} is ${self.price_for(found)}."

    # Saves one approved pickup order. Only the manager's approval calls this
    def add_order(self, item, name):
        """Record one approved pickup order. Only an approval calls this."""
        self.orders.append({"item": item, "name": name})
