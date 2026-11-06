from mock_model import MockModel
from my_assistant import RestaurantHelper
from my_tool import MenuLookup


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_helper():
    """Build a fresh helper with its own tool and a mock model for each test."""
    tool = MenuLookup({"burger": 12, "fries": 5}, "11 am to 9 pm")
    return RestaurantHelper("lexy 2.0", "Be helpful.", tool, MockModel())


def make_helper_with_silent_model():
    """Build a helper whose model never answers."""
    tool = MenuLookup({"burger": 12, "fries": 5}, "11 am to 9 pm")
    return RestaurantHelper("lexy 2.0", "Be helpful.", tool, SilentModel())


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
    helper = make_helper_with_silent_model()
    assert "try again" in helper.respond("do you have pizza")


def test_history_grows_by_two_each_turn():
    helper = make_helper()
    helper.respond("hello")
    helper.respond("what are your hours")
    assert len(helper.history) == 4


def test_other_messages_go_to_the_model():
    helper = make_helper()
    assert helper.respond("hello") == "Hello! How can I help you today?"


def test_safe_reply_when_the_model_has_no_answer():
    helper = make_helper_with_silent_model()
    assert "try again" in helper.respond("hello")


def test_price_rule_does_not_need_the_model():
    helper = make_helper_with_silent_model()
    assert helper.respond("how much is the burger") == "The burger is $12."


def test_handoff_rule_does_not_need_the_model():
    helper = make_helper_with_silent_model()
    assert "manager" in helper.respond("I want to make a reservation")
