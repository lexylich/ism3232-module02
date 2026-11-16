from fake_model import FakeModel
from my_assistant import RestaurantHelper
from my_tool import MenuLookup
from my_toolbox import MenuToolbox
from pickup_queue import PickupQueue


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def decide(self, instructions, history, tools):
        return None


def make_helper(model):
    """Build a fresh helper with its own tools and the model it is given."""
    menu_tool = MenuLookup({"burger": 12, "fries": 5}, "11 am to 9 pm")
    tools = MenuToolbox(menu_tool, PickupQueue(menu_tool))
    return RestaurantHelper("lexy 2.0", "Be helpful.", tools, model)


def ask_for_tool(name, arguments):
    """Build the decision a model returns when it wants a tool."""
    return {"tool": name, "arguments": arguments}


def test_model_can_ask_for_a_price():
    model = FakeModel(
        [ask_for_tool("look_up_price", {"item": "burger"}), {"text": "It is $12."}]
    )
    helper = make_helper(model)
    helper.respond("how much is the burger")
    assert helper.history[1]["content"] == "The burger is $12."


def test_pickup_order_waits_for_the_manager():
    model = FakeModel(
        [
            ask_for_tool(
                "request_pickup_order", {"item": "burger", "name": "Dana Cruz"}
            ),
            {"text": "Sent."},
        ]
    )
    helper = make_helper(model)
    helper.respond("Pickup order for a burger for Dana Cruz")
    assert len(helper.tools.pickup_queue.waiting()) == 1
    assert helper.tools.menu_tool.orders == []


def test_made_up_name_is_refused():
    model = FakeModel(
        [
            ask_for_tool(
                "request_pickup_order", {"item": "burger", "name": "Jane Doe"}
            ),
            {"text": "What name?"},
        ]
    )
    helper = make_helper(model)
    helper.respond("I want to pick up a burger")
    assert "has not given that name" in helper.history[1]["content"]
    assert helper.tools.pickup_queue.waiting() == []


def test_approval_places_the_order_once():
    menu_tool = MenuLookup({"burger": 12}, "11 am to 9 pm")
    queue = PickupQueue(menu_tool)
    queue.request_pickup_order("burger", "Dana Cruz")
    queue.approve(1)
    queue.approve(1)
    assert len(menu_tool.orders) == 1


def test_reservation_goes_to_the_manager():
    helper = make_helper(FakeModel([]))
    assert "manager" in helper.respond("I want to make a reservation")


def test_hours_rule_does_not_need_the_model():
    helper = make_helper(FakeModel([]))
    assert "11 am to 9 pm" in helper.respond("what are your hours")


def test_unknown_tool_is_refused():
    model = FakeModel(
        [ask_for_tool("delete_menu", {"item": "burger"}), {"text": "Sorry."}]
    )
    helper = make_helper(model)
    helper.respond("Please delete the burger")
    assert helper.history[1]["content"] == "There is no tool named delete_menu."


def test_safe_reply_when_the_model_has_no_answer():
    helper = make_helper(SilentModel())
    assert "try again" in helper.respond("do you have pizza")


def test_loop_stops_after_three_tool_rounds():
    request = ask_for_tool("look_up_price", {"item": "burger"})
    helper = make_helper(FakeModel([request, request, request]))
    reply = helper.respond("how much is the burger")
    assert "manager" in reply
    assert len(helper.history) == 5
