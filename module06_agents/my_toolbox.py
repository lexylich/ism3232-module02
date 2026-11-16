# my_toolbox.py
# Author: Lexy Lichtenstein


class MenuToolbox:
    """Every tool request from the model comes through here and is checked."""

    # Saves the two tools the model is allowed to use
    def __init__(self, menu_tool, pickup_queue):
        """Hold the tools the model is allowed to ask for."""
        self.menu_tool = menu_tool
        self.pickup_queue = pickup_queue

    # Lists the methods without parentheses so they are passed along, not called
    def tool_list(self):
        """Return the tools the model may ask for. They are not called here."""
        return [
            self.menu_tool.look_up_price,
            self.pickup_queue.request_pickup_order,
        ]

    # The one checked door: it refuses bad requests before any tool runs
    def run(self, name, arguments, history):
        """Check one tool request. Run the tool only if every check passes."""
        if name == "look_up_price":
            item = self.clean(arguments, "item")
            if item == "":
                return "The item is missing. Ask the customer which item."
            return self.menu_tool.look_up_price(item)
        if name == "request_pickup_order":
            item = self.clean(arguments, "item")
            customer_name = self.clean(arguments, "name")
            # The empty check must come first, because "" is inside every string
            if item == "" or customer_name == "":
                return "The item and the customer's name are both needed."
            if not self.customer_said(history, item):
                return "The customer has not given that item. Ask them for it."
            if not self.customer_said(history, customer_name):
                return "The customer has not given that name. Ask them for it."
            return self.pickup_queue.request_pickup_order(item, customer_name)
        return f"There is no tool named {name}."

    # Turns one argument into text without extra spaces, or "" if it is missing
    def clean(self, arguments, key):
        """Return one argument as text without extra spaces, or "" if it is missing."""
        return str(arguments.get(key, "")).strip()

    # True only if the text appears in a message the customer typed
    def customer_said(self, history, text):
        """Return True if text appears in a message the customer typed."""
        for message in history:
            if message["role"] == "user" and text.lower() in message["content"].lower():
                return True
        return False
