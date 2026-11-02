from my_assistant import RestaurantHelper
from my_tool import MenuLookup


def make_helper():
    """Build a fresh helper with its own tool for each test."""
    tool = MenuLookup({"burger": 12, "fries": 5}, "11 am to 9 pm")
    return RestaurantHelper("lexy 2.0", "Be helpful.", tool)


def test_price_question_uses_the_tool():
    helper = make_helper()
    assert helper.respond("how much is the burger") == "The burger is $12."


def test_price_question_without_an_item_asks_for_one():
    helper = make_helper()
    assert "Which item?" in helper.respond("how much is it")


def test_reservation_goes_to_the_manager():
    helper = make_helper()
    assert "manager" in helper.respond("I want to make a reservation")


def test_unknown_request_gets_a_safe_reply():
    helper = make_helper()
    assert "not sure" in helper.respond("do you have pizza")


def test_history_grows_by_two_each_turn():
    helper = make_helper()
    helper.respond("hello")
    helper.respond("what are your hours")
    assert len(helper.history) == 4
