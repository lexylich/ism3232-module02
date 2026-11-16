# ollama_model.py
# Author: Lexy Lichtenstein

from ollama import ResponseError, chat


class OllamaModel:
    """A real AI model that runs on this computer through Ollama."""

    def __init__(self, model_name):
        """Remember which model to ask."""
        self.model_name = model_name

    def reply(self, instructions, history):
        """Send the instructions and the conversation to the model. Return its reply."""
        messages = [{"role": "system", "content": instructions}]
        messages = messages + history
        try:
            response = chat(model=self.model_name, messages=messages)
        except ConnectionError:
            return None
        except ResponseError:
            return None
        return response.message.content

    def decide(self, instructions, history, tools):
        """Send the conversation and the tools. Return a reply or a tool request."""
        messages = [{"role": "system", "content": instructions}]
        for entry in history:
            if entry["role"] == "tool":
                messages.extend(self.tool_messages(entry))
            else:
                messages.append(entry)
        try:
            response = chat(model=self.model_name, messages=messages, tools=tools)
        except (ConnectionError, ResponseError):
            return None
        message = response.message
        if message.tool_calls:
            first = message.tool_calls[0]
            return {"tool": first.function.name, "arguments": first.function.arguments}
        return {"text": message.content}

    def tool_messages(self, entry):
        """Turn one tool entry from the history into the two messages Ollama expects."""
        call = {
            "function": {"name": entry["tool_name"], "arguments": entry["arguments"]}
        }
        return [
            {"role": "assistant", "content": "", "tool_calls": [call]},
            {
                "role": "tool",
                "tool_name": entry["tool_name"],
                "content": entry["content"],
            },
        ]
