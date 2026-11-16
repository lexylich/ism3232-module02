# Week 12 answers

## Exercise 1

1. The messages the customer typed: "I want to change my shipping address", "It's order A102", and "9 Pine Street, Tampa".
2. Two tool requests were refused, because the model used an order ID and an address the customer never typed.
3. Ollama receives 14 messages on the next call: 1 system message, 4 user messages (including "thanks"), 3 assistant messages, and 6 messages from the 3 tool entries (each tool entry becomes the model's request plus the tool's result).
4. "Do you sell gift cards?" contains the word "card", so the payment rule sends it to a person before the model sees it. That is acceptable because a false alarm only costs a short wait, while a missed payment question could expose card details.

## Exercise 3

Terminal output with the check turned off:

    Type a message, or type quit to stop.
    You: I want to change my shipping address
    Sunny: Your request to change the shipping address has been submitted and is awaiting staff approval.
    You: quit
    Messages in this conversation: 3
    Staff review
    Request 1: A100 to 123 Main St, Anytown, AN 12345
    Approve? yes or no: no
    Request 1 rejected.
    A100 14 Bay Road
    A101 3 Gull Lane
    A102 88 Pier Street

Note: With the check off, the model made up an order ID (A100) and an address (123 Main St, Anytown, AN 12345) that I never typed, and filed a request with them. That matters because a busy staff member could approve it and send a customer's order to an address nobody gave. I rejected it, so no address changed. The check costs one extra question to the customer, and the approval queue is only a second line of defence.