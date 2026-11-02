# my_tool.py
# Author: Lexy Lichtenstein


class MenuLookup:
    """A tool that knows the menu and hours. It knows nothing about chatting."""

    # Saves the menu and hours on this object so the other methods can use them
    def __init__(self, menu, hours):
        """Store the menu (item to price) and the opening hours."""
        self.menu = menu
        self.hours = hours

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
