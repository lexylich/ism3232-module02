# my_assistant.py
# Author: Lexy Lichtenstein

# Words that mean a person must handle the request
HANDOFF_WORDS = ["reservation", "reserve", "complaint", "refund", "allergy"]


class RestaurantHelper:
    """A mock restaurant helper. Its replies come from simple rules, not from AI."""

    # Saves the name, instructions, menu tool, and an empty history on this helper
    def __init__(self, name, instructions, menu_tool):
        """Set up one helper with its own name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.menu_tool = menu_tool
        self.history = []

    # Records the customer's message, gets a reply, records it, and returns it
    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    # Checks the rules in order: handoff first, then hours, then prices, then hello
    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to the manager."
        if "hours" in text or "open" in text:
            return f"We are open {self.menu_tool.get_hours()}."
        if "price" in text or "cost" in text or "how much" in text:
            return self.price_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. Ask me about our menu prices or hours."
        return "I'm not sure how to help with that. I can share prices and hours."

    # Returns True if any handoff word appears in the message
    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    # Asks the tool for the item and its price, and asks which item if none is found
    def price_reply(self, user_message):
        """Use the menu tool to answer a question about a price."""
        item = self.menu_tool.find_item(user_message)
        if item is None:
            return "Which item? Please name a menu item like burger."
        price = self.menu_tool.price_for(item)
        return f"The {item} is ${price}."
