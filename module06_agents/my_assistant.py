# my_assistant.py
# Author: Lexy Lichtenstein

# Words that mean a person must handle the request
HANDOFF_WORDS = ["reservation", "reserve", "complaint", "refund", "allergy"]
# The most tool requests the helper will run for one reply
MAX_TOOL_ROUNDS = 3


class RestaurantHelper:
    """A restaurant helper. Rules handle what must be right. A model handles the rest."""

    # Saves the name, instructions, toolbox, model, and an empty history on this helper
    def __init__(self, name, instructions, tools, model):
        """Set up one helper with its own name, instructions, tools, model, and history."""
        self.name = name
        self.instructions = instructions
        self.tools = tools
        self.model = model
        self.history = []

    # Records the customer's message, gets a reply, records it, and returns it
    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    # Checks the rules in order: handoff first, then hours, then the model
    def choose_reply(self, user_message):
        """Use a rule when one applies. Otherwise ask the model."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to the manager."
        if "hours" in text or "open" in text:
            return f"We are open {self.tools.menu_tool.get_hours()}."
        return self.model_reply()

    # Asks the model what to do, runs any tool it asks for, and asks again, up to the limit
    def model_reply(self):
        """Ask the model. Run each tool it asks for, then ask again, up to a limit."""
        rounds = 0
        while rounds < MAX_TOOL_ROUNDS:
            tool_list = self.tools.tool_list()
            decision = self.model.decide(self.instructions, self.history, tool_list)
            # None means the model is unavailable, so give a safe answer
            if decision is None:
                return "Sorry, I can't answer that right now. Please try again in a moment."
            # A text decision is the final reply
            if "text" in decision:
                return decision["text"]
            # Otherwise the model asked for a tool, so the toolbox checks and runs it
            name = decision["tool"]
            arguments = decision["arguments"]
            result = self.tools.run(name, arguments, self.history)
            # The result is saved as a tool entry so the history shows where the answer came from
            self.history.append(
                {
                    "role": "tool",
                    "tool_name": name,
                    "arguments": arguments,
                    "content": result,
                }
            )
            rounds += 1
        return "Sorry, I couldn't finish that. I'm passing you to the manager."

    # Returns True if any handoff word appears in the message
    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False
