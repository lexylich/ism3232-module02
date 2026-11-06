# my_main.py
# Author: Lexy Lichtenstein

from my_assistant import RestaurantHelper
from my_tool import MenuLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are lexy 2.0, an assistant for a small restaurant.
Answer in one short sentence.
The restaurant is on Ocean Drive in South Beach, Miami, one block from the beach.
Takeout orders are ready about 15 minutes after you order.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to the manager."""

MENU = {
    "burger": 12,
    "fries": 5,
    "salad": 9,
    "milkshake": 6,
}

HOURS = "11 am to 9 pm every day"

menu_tool = MenuLookup(MENU, HOURS)
model = OllamaModel(MODEL_NAME)
helper = RestaurantHelper("lexy 2.0", INSTRUCTIONS, menu_tool, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")
