import tkinter as tk
import itertools


class MicAnimation:
    """
    Simple animated microphone indicator
    """

    def __init__(self, parent):

        self.parent = parent

        self.label = tk.Label(
            parent,
            text="🎤",
            font=("Segoe UI Emoji", 32),
            fg="red"
        )

        self.label.pack(pady=10)

        # Animation states
        self.states = ["🎤", "🔴", "⚫", "🔴"]
        self.animation = itertools.cycle(self.states)

        self.running = False

    def start(self):
        """
        Start animation
        """
        self.running = True
        self.animate()

    def stop(self):
        """
        Stop animation
        """
        self.running = False
        self.label.config(text="🎤")

    def animate(self):
        """
        Animation loop
        """

        if not self.running:
            return

        self.label.config(text=next(self.animation))

        self.parent.after(300, self.animate)