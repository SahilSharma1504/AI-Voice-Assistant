import tkinter as tk
import itertools


class TypingAnimation:
    """
    ChatGPT-like typing indicator animation
    Example: AI is typing...
    """

    def __init__(self, parent):

        self.parent = parent

        self.label = tk.Label(
            parent,
            text="AI is typing",
            font=("Segoe UI", 10, "italic"),
            fg="gray"
        )

        self.label.pack(pady=5)

        self.states = [
            "AI is typing",
            "AI is typing.",
            "AI is typing..",
            "AI is typing..."
        ]

        self.animation = itertools.cycle(self.states)

        self.running = False

    def start(self):
        """
        Start typing animation
        """
        self.running = True
        self.animate()

    def stop(self):
        """
        Stop typing animation
        """
        self.running = False
        self.label.config(text="")

    def animate(self):

        if not self.running:
            return

        self.label.config(text=next(self.animation))

        self.parent.after(400, self.animate)