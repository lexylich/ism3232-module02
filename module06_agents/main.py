# main.py
# Author: Lexy Lichtenstein

from change_queue import ChangeQueue
from chatbot import SupportChatbot
from fallback_model import FallbackModel
from keyword_model import KeywordModel
from ollama_model import OllamaModel
from order_tool import OrderLookup
from stock_tool import StockLookup
from toolbox import Toolbox

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Sunny, the support assistant for Bayside Outfitters.
Reply in one short sentence.
Store hours run from 10 am to 7 pm, every day of the week.
Returns are accepted for 30 days when the customer has a receipt.
Use only facts from these instructions or from tool results.
When you are unsure, say so and offer to connect the customer with a human agent."""

ORDERS = {
    "A100": {"status": "shipped", "address": "14 Bay Road"},
    "A101": {"status": "processing", "address": "3 Gull Lane"},
    "A102": {"status": "delivered", "address": "88 Pier Street"},
}

STOCK = {
    "rain jacket": 12,
    "day pack": 0,
    "trail hat": 5,
}

order_tool = OrderLookup(ORDERS)
stock_tool = StockLookup(STOCK)
change_queue = ChangeQueue(order_tool)
tools = Toolbox(order_tool, stock_tool, change_queue)
model = FallbackModel(OllamaModel(MODEL_NAME), KeywordModel())
bot = SupportChatbot("Sunny", INSTRUCTIONS, tools, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")

print("Staff review")
for request in change_queue.waiting():
    number = request["number"]
    print(f"Request {number}: {request['order_id']} to {request['new_address']}")
    answer = input("Approve? yes or no: ")
    if answer == "yes":
        print(change_queue.approve(number))
    else:
        print(change_queue.reject(number))

for order_id, details in ORDERS.items():
    print(order_id, details["address"])
