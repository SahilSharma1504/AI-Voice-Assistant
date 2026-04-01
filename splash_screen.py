import tkinter as tk
from tkinter import ttk
import time
import threading
import assistant_gui


def start_main_app(root):
    root.destroy()
    assistant_gui.main()


def splash():

    root = tk.Tk()
    root.title("Starting AI Assistant")
    root.geometry("500x300")
    root.configure(bg="#202123")

    root.overrideredirect(True)  # removes window border

    # Center window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (500 // 2)
    y = (screen_height // 2) - (300 // 2)

    root.geometry(f"500x300+{x}+{y}")

    # Title
    title = tk.Label(
        root,
        text="AI Assistant",
        font=("Segoe UI", 24, "bold"),
        fg="white",
        bg="#202123"
    )
    title.pack(pady=40)

    # Subtitle
    subtitle = tk.Label(
        root,
        text="Initializing...",
        font=("Segoe UI", 12),
        fg="gray",
        bg="#202123"
    )
    subtitle.pack(pady=10)

    # Progress bar
    style = ttk.Style()
    style.theme_use("default")
    style.configure(
        "TProgressbar",
        troughcolor="#202123",
        background="#10A37F",
        thickness=8
    )

    progress = ttk.Progressbar(
        root,
        orient="horizontal",
        length=300,
        mode="determinate"
    )
    progress.pack(pady=20)

    def load():

        for i in range(101):
            time.sleep(0.02)
            progress["value"] = i
            root.update_idletasks()

        root.after(200, lambda: start_main_app(root))

    threading.Thread(target=load).start()

    root.mainloop()


if __name__ == "__main__":
    splash()