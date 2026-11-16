# fake_model.py
# Author: Lexy Lichtenstein


class FakeModel:
    """A test model that returns a scripted list of decisions in order."""

    def __init__(self, decisions):
        """Store the scripted decisions and start the call count at zero."""
        self.decisions = decisions
        self.calls = 0

    def decide(self, instructions, history, tools):
        """Return the next scripted decision and count this call."""
        decision = self.decisions[self.calls]
        self.calls += 1
        return decision
