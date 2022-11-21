import cohere
from revise.model import get_feedback

class ReviseBot():
    """A class yielding writing feedback generating conversational agents"""

    def __init__(self, cohere_api_key, text=""):
        self._cohere_api_key = cohere_api_key
        self._text = text
        self._chat_history = []
        self._co = cohere.Client(self._cohere_api_key)
    
    @property
    def chat_history(self):
        return self._chat_history

    def set_chat_history(self, chat_history):
        self._chat_history = chat_history

    @property
    def text(self):
        return self._text
    
    def set_text(self, text):
        self._text = text

    def answer(self, question):
        """Answer a question, based on recent conversational history."""

        self.chat_history.append("user: " + question)

        if self._text == "":
            reply = "Text is required for feedback"
            self._chat_history.append("bot: " + reply)
            return reply

        history = "\n".join(self.chat_history[-6:])

        reply = get_feedback(history, self._text, self._co)

        self._chat_history.append("bot: " + reply)

        return reply