# keyword_model.py
# Author: Lexy Lichtenstein


class KeywordModel:
    """Makes decisions from simple keyword checks. Needs no AI service."""

    def decide(self, instructions, history, tools):
        """Pick a reply or a tool request based on the newest entry in history."""
        newest = history[-1]
        if newest["role"] == "tool":
            # A tool has already run, so show its result to the customer.
            return {"text": newest["content"]}
        message = newest["content"]
        lowered = message.lower()
        if "order" in lowered:
            return {"tool": "look_up_order", "arguments": {"order_id": message}}
        if "stock" in lowered:
            return {"tool": "check_stock", "arguments": {"item": message}}
        if "hello" in lowered:
            return {"text": "Hello! How can I help you today?"}
        return {
            "text": "I'm not sure how to help with that. I can check an order or stock."
        }
