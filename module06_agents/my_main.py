# my_main.py
# Author: Lexy Lichtenstein

from my_assistant import RestaurantHelper
from my_tool import MenuLookup

MENU = {
    "burger": 12,
    "fries": 5,
    "salad": 9,
    "milkshake": 6,
}

HOURS = "11 am to 9 pm every day"

menu_tool = MenuLookup(MENU, HOURS)
helper = RestaurantHelper(
    "lexy 2.0",
    "You help customers of a small restaurant with menu prices and hours.",
    menu_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{helper.name}: {helper.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(helper.history)}")
