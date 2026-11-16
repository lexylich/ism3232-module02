# my_main.py
# Author: Lexy Lichtenstein

from my_assistant import RestaurantHelper
from my_tool import MenuLookup
from my_toolbox import MenuToolbox
from ollama_model import OllamaModel
from pickup_queue import PickupQueue

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are lexy 2.0, the assistant for a small restaurant.
Reply in one short sentence.
If the customer only says hello, greet them and ask how you can help.
To request a pickup order you need the menu item and the customer's name.
Use only facts from these instructions or from tool results.
When you are unsure, say so and offer to connect the customer with the manager."""

MENU = {"burger": 12, "fries": 5, "milkshake": 6}
HOURS = "11 am to 9 pm"

menu_tool = MenuLookup(MENU, HOURS)
pickup_queue = PickupQueue(menu_tool)
tools = MenuToolbox(menu_tool, pickup_queue)
model = OllamaModel(MODEL_NAME)
helper = RestaurantHelper("lexy 2.0", INSTRUCTIONS, tools, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")

print("Manager review")
for request in pickup_queue.waiting():
    number = request["number"]
    print(f"Request {number}: {request['name']} wants a {request['item']}")
    answer = input("Approve? yes or no: ")
    if answer == "yes":
        print(pickup_queue.approve(number))
    else:
        print(pickup_queue.reject(number))

print(f"Pickup orders: {len(menu_tool.orders)}")

# Shows each tool request the model made and what the toolbox answered
for entry in helper.history:
    if entry["role"] == "tool":
        print(entry["tool_name"], entry["arguments"], entry["content"])
