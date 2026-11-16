# pickup_queue.py
# Author: Lexy Lichtenstein


class PickupQueue:
    """Pickup orders waiting for the manager to approve. Nothing is ordered until then."""

    # Saves the menu tool (approved orders go into it) and starts with no requests
    def __init__(self, menu_tool):
        """Start with no requests. Approved orders go through the menu tool."""
        self.menu_tool = menu_tool
        self.requests = []

    # Files a request with the status "waiting". It does not place the order
    def request_pickup_order(self, item, name):
        """Ask the manager to approve a pickup order. The manager must approve it.

        Args:
            item: The menu item, like burger.
            name: The customer's name for the order.
        """
        # Refuses items that are not on the menu
        found = self.menu_tool.find_item(item)
        if found is None:
            return "That item is not on the menu. Try an item like burger."
        # Numbers the request and files it as waiting
        number = len(self.requests) + 1
        request = {"number": number, "item": found, "name": name, "status": "waiting"}
        self.requests.append(request)
        return f"Request {number} was sent to the manager. Nothing is ordered yet."

    # Returns only the requests that still need a decision
    def waiting(self):
        """Return the requests that are still waiting for a decision."""
        result = []
        for request in self.requests:
            if request["status"] == "waiting":
                result.append(request)
        return result

    # Finds one request by its number, or None if there is no such request
    def find(self, number):
        """Return the request with this number, or None."""
        for request in self.requests:
            if request["number"] == number:
                return request
        return None

    # The only code that places an order. It refuses a request that was already decided
    def approve(self, number):
        """Approve one waiting request and place the order."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "approved"
        self.menu_tool.add_order(request["item"], request["name"])
        return f"Request {number} approved."

    # Marks a waiting request as rejected and places nothing
    def reject(self, number):
        """Reject one waiting request. Nothing is ordered."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "rejected"
        return f"Request {number} rejected."
